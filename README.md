# tools

This is a collection of the tools I used while studying for, and taking the OSCP. 

## Setup
```bash
cd /opt
sudo git clone https://github.com/tm-security/tools.git
sudo chown -R kali:kali /opt/tools
```

## How to Use
I would then use [wwwtree](https://github.com/t3l3machus/wwwtree) to quickly host the files like this:
```bash
┌──(kali㉿kali)-[/opt/tools]
└─$ ./wwwtree.py -r /opt/tools -i eth0 -q
[Info] Http server listening on 0.0.0.0:80, Interface addr: 192.168.1.2
[Info] Press ENTER to exit.

/opt/tools/ (web root)
├── http://192.168.154.133:80/wwwtree.py
├── active_directory/
│   ├── http://192.168.154.133:80/active_directory/PowerView.ps1
│   ├── http://192.168.154.133:80/active_directory/Rubeus.exe
│   ├── http://192.168.154.133:80/active_directory/SharpHound.exe
│   ├── http://192.168.154.133:80/active_directory/SharpHound.ps1
│   └── http://192.168.154.133:80/active_directory/mimikatz.exe
├── linux/
│   ├── http://192.168.154.133:80/linux/LinEnum.sh
│   ├── http://192.168.154.133:80/linux/les.sh
│   ├── http://192.168.154.133:80/linux/linpeas.sh
│   └── http://192.168.154.133:80/linux/pspy64
├── scripts/
│   ├── http://192.168.154.133:80/scripts/encoded-ps-rev.py
│   └── http://192.168.154.133:80/scripts/transfer.ps1
├── shells/
│   └── http://192.168.154.133:80/shells/shell.php
├── tunnel/
│   ├── linux/
│   │   ├── http://192.168.154.133:80/tunnel/linux/ligolo-lin-agent
│   │   └── http://192.168.154.133:80/tunnel/linux/ligolo-lin-proxy
│   └── windows/
│       ├── http://192.168.154.133:80/tunnel/windows/ligolo-win-agent.exe
│       └── http://192.168.154.133:80/tunnel/windows/ligolo-win-proxy.exe
└── windows/
        ├── http://192.168.154.133:80/windows/GodPotato.exe
        ├── http://192.168.154.133:80/windows/PowerUp.ps1
        ├── http://192.168.154.133:80/windows/PrintSpoofer64.exe
        ├── http://192.168.154.133:80/windows/Seatbelt.exe
        ├── http://192.168.154.133:80/windows/nc.exe
        └── http://192.168.154.133:80/windows/winPEASany.exe
```

Thank you to the following repositories for all of these great tools!
- https://github.com/t3l3machus
- https://github.com/ParrotSec
- https://github.com/PowerShellEmpire
- https://github.com/GhostPack
- https://github.com/BloodHoundAD
- https://github.com/The-Z-Labs
- https://github.com/rebootuser
- https://github.com/carlospolop
- https://github.com/DominicBreuker
- https://github.com/nicocha30
- https://github.com/carlospolop
- https://github.com/itm4n
