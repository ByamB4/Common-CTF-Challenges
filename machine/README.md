# Machine / Enumeration

Host discovery, enumeration, and privesc helpers (mostly Linux).

## Quick wins
- Run one fast enumerator (LinPEAS/LinEnum) and one exploit suggester early.
- Check SUID binaries, scheduled tasks, writable configs, and password reuse.
- If WordPress is present, enumerate plugins/themes/users quickly with wpscan.

## Automated enumeration
- [LinPEAS](https://github.com/carlospolop/privilege-escalation-awesome-scripts-suite/tree/master/linPEAS)
- [LinEnum](https://github.com/rebootuser/LinEnum)
- [LES (Linux Exploit Suggester)](https://github.com/mzet-/linux-exploit-suggester)
- [Linux Smart Enumeration](https://github.com/diego-treitos/linux-smart-enumeration)
- [Linux Priv Checker](https://github.com/linted/linuxprivchecker)

## Be root
- PwnKit: https://github.com/ly4k/PwnKit

## SUID hunting
- `find / -perm -4000 2>/dev/null`

## Directory / host discovery
- `subfinder -d hackerone.com -v`
- `waybackurls hackerone.com`

## WordPress
- wpscan aggressive sweep:
  ```
  wpscan --rua -e ap,at,tt,cb,dbe,u,m --url https://target.com \
    --plugins-detection aggressive --api-token <API_TOKEN> \
    --passwords ~/SecLists/Passwords/probable-v2-top1575.txt
  ```
- Interesting endpoints: `/wp-login.php`, `/wp-admin`, `/xmlrpc.php`, `/wp-json/oembed/1.0/proxy`

## Defense snippets (blue team quick checks)
- Top CPU: `ps -e -o pcpu,cpu,nice,state,cputime,args --sort pcpu | sed '/^ 0.0 /d'| tac | head -5`
- Top CPU (alt): `ps auxf | sort -nr -k 3 | head -5`
- Top memory: `ps -e -orss=,args= | sort -b -k1,1n | pr -TW$COLUMNS | tac | head -5`
- Top memory (alt): `ps auxf | sort -nr -k 4 | head -5`
- Process tree: `ps -x --forest`
- Network status: `netstat -alptn`
