import pyshark

def extract_dns_requests(pcap_file):
    cap = pyshark.FileCapture(pcap_file, display_filter="dns")
    
    dns_requests = []
    
    for packet in cap:
        try:
            if hasattr(packet, 'dns') and hasattr(packet.dns, 'qry_name'):
                dns_requests.append(packet.dns.qry_name)
        except AttributeError:
            continue
    
    cap.close()
    return dns_requests

pcap_path = "query.pcap"
dns_queries = extract_dns_requests(pcap_path)

for query in dns_queries:
    print(query)
