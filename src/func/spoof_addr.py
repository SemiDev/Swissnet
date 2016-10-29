import os
import threading
from random import randint
import traceback

def spoof_addr(terminal=None):
    try:
        router_ip = os.popen("ip route show | grep -i 'default via'| awk '{print $3 }'").read()
        router_ip = router_ip.strip()
        nlist = router_ip.split(".")
        try:
            spoofed_addr = nlist[0]+'.'+nlist[1]+'.'+nlist[2]+'.'+str(randint(1,254))
            return spoofed_addr
        except IndexError:
            terminal.write("\n[-] Could not spoof an address!\n[-] Exiting")
            exit()
    except Exception as s:
        terminal.write('\n'+str(s))
        traceback.print_exc()
