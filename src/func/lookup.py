import os
import socket
from func.get_mac import get_mac

def lookup(host):
    exitstat = os.system('fping '+host)
    if not exitstat:
        try:
            name, alias, addr = socket.gethostbyaddr(host.strip())
            if not alias: 
                alias = 'unknown'
            print("Hostname // "+name+" | Aliases // "+str(alias)+" | Address // "+addr[0]+" | HWAddress // "+get_mac(host))
        except:
            print("[*] Could not find a hostname")
            try:
                print("Address // "+host+" | HWAddress // "+get_mac(host))
            except TypeError:
                print("[-] Could not find a mac address. IP may not be connected to network")
                print("Address // "+host)
    else:
        print("[-] Error: Host not found")
