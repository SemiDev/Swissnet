import os
import socket
from func.get_mac import get_mac

def lookup(host,terminal=None):
    exitstat = os.system('fping '+host)
    if not exitstat:
        try:
            name, alias, addr = socket.gethostbyaddr(host.strip())
            if not alias: 
                alias = 'unknown'
            if terminal == None:
                print("Hostname // "+name+" | Aliases // "+str(alias)+" | Address // "+addr[0]+" | HWAddress // "+get_mac(host))
            else:
                terminal.configure(text=terminal.cget("text")+"\nHostname // "+name+" | Aliases // "+str(alias)+" | Address // "+addr[0]+" | HWAddress // "+get_mac(host))
        except:
            if terminal == None:
                print("[*] Could not find a hostname")
            else:
                terminal.configure(text=terminal.cget("text")+'\n[*] Could not find a hostname')
            try:
                if terminal == None:
                    print("Address // "+host+" | HWAddress // "+get_mac(host))
                else:
                    terminal.configure(text=terminal.cget("text")+"\n Address // "+host+" | HWAddress // "+get_mac(host))
            except TypeError:
                if terminal == None:
                    print("[-] Could not find a mac address")
                    print("Address // "+host)
                else:
                    terminal.configure(text=terminal.cget("text")+'\n[-] Could not find a mac address\nAddress // '+host)
    else:
        if terminal == None:
            print("[-] Error: Host not found")
        else:
            terminal.configure(text=terminal.cget("text")+'\n[-] Error: Host not found')
