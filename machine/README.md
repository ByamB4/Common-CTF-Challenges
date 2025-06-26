### Automated Enumeration Tools

- [LinPeas](https://github.com/carlospolop/privilege-escalation-awesome-scripts-suite/tree/master/linPEAS)
- [LinEnum](https://github.com/rebootuser/LinEnum)
- [LES (Linux Exploit Suggester)](https://github.com/mzet-/linux-exploit-suggester)
- [Linux Smart Enumeration](https://github.com/diego-treitos/linux-smart-enumeration)
- [Linux Priv Checker](https://github.com/linted/linuxprivchecker)

### Be root

- [https://github.com/ly4k/PwnKit](https://github.com/ly4k/PwnKit)

### Find SUID binaries

  - `find / -perm -4000 2>/dev/null`

## Directory finder
  - `subfinder -d hackerone.com -v`
  - `waybackurls hackerone.com`

### Wordpress

  - **wpscan**
    - `wpscan --rua -e ap,at,tt,cb,dbe,u,m --url https://target.com --plugins-detection aggressive --api-token <API_TOKEN> --passwords ~/SecLists/Passwords/probable-v2-top1575.txt`

  - **Interesting endpoints**
    - `/wp-login.php`
    - `/wp-login`
    - `/wp-admin`
    - `/wp-admin.php`
    - `/login`
    - `/xmlrpc.php`
    - `/wp-json/oembed/1.0/proxy`
   
### Defense cheat sheets

  - **Get top 5 processes by CPU usage**
    - `ps -e -o pcpu,cpu,nice,state,cputime,args --sort pcpu | sed '/^ 0.0 /d'| tac | head -5`
    - `ps auxf | sort -nr -k 3 | head -5`
   
  - **Get top 5 processes by memory usage**
    - `ps -e -orss=,args= | sort -b -k1,1n | pr -TW$COLUMNS| tac | head -5`
    - `ps auxf | sort -nr -k 4 | head -5`

  - **Tree view**
    - `ps -x --forest`

  - **Show network status**
    - `netstat -alptn`
