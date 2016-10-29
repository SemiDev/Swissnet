import os
import socket
from func.get_mac import get_mac
import traceback

def lookup(host,terminal):
    try:
        exitstat = os.system('fping '+host)
        if not exitstat:
            try:
                name, alias, addr = socket.gethostbyaddr(host.strip())
                if not alias:
                    alias = 'unknown'
                terminal.write("\nHostname // "+name+" | Aliases // "+str(alias)+" | Address // "+addr[0]+" | HWAddress // "+get_mac(host))
            except:
                terminal.write('\n[*] Could not find a hostname')
                try:
                    terminal.write("\n Address // "+host+" | HWAddress // "+get_mac(host))
                except TypeError:
                    terminal.write('\n[-] Could not find a mac address\nAddress // '+host)
        else:
            terminal.write('\n[-] Error: Host not found')
    except Exception as s:
        terminal.write('\n'+str(traceback.print_exc()))
