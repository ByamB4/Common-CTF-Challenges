# Common CTF Challenges

Reference notes, commands, and ready-to-use snippets for common Capture the Flag categories. Keep it locally, search fast, and copy what you need mid-challenge.

## Repo at a glance
- `crypto/` cipher references, substitution charts, example ciphertexts, and stream/symmetric crypto hints
- `steganography/` image/audio steg tools and quick links
- `web/` web exploitation tricks (LFI, XSS, SQLi, SSTI, prototype pollution) and payload examples
- `pwn/` binary exploitation reminders: mitigations, syscall tables, shellcode links
- `reverse/` reversing cheats for Python, Rust/Go, and general tooling
- `mobile/` Android-focused reversing and runtime manipulation (APK rebuilds, Frida hooks, Hermes bytecode)
- `crack/` cracking commands for hashes, KeePass, Wi-Fi captures, and services
- `machine/` enumeration and privesc helpers (Linux), WordPress scanning, defense snippets
- `network/mitm.py` Scapy MITM automation for intercepting and injecting on a TCP service (run with root)
- `cloud/`, `osint/`, `forensics/`, `misc/`, `esolangs/`, `jailbreak/`, `web3/` focused notes and links for their respective categories

## Directory map
- Cheatsheets: `cloud/`, `crack/`, `crypto/`, `esolangs/`, `forensics/`, `jailbreak/`, `machine/`, `misc/`, `mobile/`, `osint/`, `pwn/`, `reverse/`, `steganography/`, `web/`, `web3/`
- Scripts: `network/mitm.py` (TCP MITM), add new tools alongside their category README
- Infrastructure: `.gitignore`, `.gitattributes` (safe to ignore while browsing)

## Quick start
- Clone and browse: `git clone https://github.com/ByamB4/Common-CTF-Challenges.git && cd Common-CTF-Challenges`.
- Search for a keyword/payload: `rg -n "pickle"`, `rg -n "sql" web`.
- View a category sheet: `less web/README.md`, `less crypto/README.md`.
- Python helpers: create a venv if you plan to run scripts: `python3 -m venv .venv && source .venv/bin/activate`.
- Run the included MITM demo: `pip install scapy`, adjust IP/MACs in `network/mitm.py`, then run with `sudo python3 network/mitm.py`.

## How to use this repo during a CTF
- Identify the category, jump into the matching folder, and scan the payloads or tool links.
- Start with the minimal commands provided (e.g., LFI payloads, hashcat modes, ARP spoofing script) before building custom exploits.
- Copy/reference only what you need; the lists are intentionally terse to stay fast during live play.
- Keep the repo locally so you can operate offline if the event restricts Internet access.
 - Add your own annotations inline so teammates know what worked in the moment.

## Contributing
- Add new material to the closest category directory. Include a short README snippet or inline comment that explains usage and prerequisites.
- Prefer runnable examples over long text. If adding scripts, keep dependencies lightweight and list install commands.
- Test what you add (hashcat modes, python snippets, etc.) and note any assumptions (OS, permissions, sample inputs).
- Open a PR from a feature branch with a clear description of what changed and why it helps CTF players.

## Notes
- Use these materials ethically and only in competitions or lab environments where you have permission.
- Links are provided for convenience; mirror important payloads locally if you expect to be offline.
