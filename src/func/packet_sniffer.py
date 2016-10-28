from __future__ import print_function
from scapy.all import *

def sniff_packets(filt,terminal=None):

    if terminal == None:
        print("[+] Packet Sniffer Started")
        print("[+] Filter: "+filt)
    else:
        terminal.configure(text=terminal.cget("text")+'\n[+] Packet Sniffer Started\n[+] Filter: '+filt)
    if filt != 'all':
        while True:
            a = sniff(filter=filt,count=1,prn=lambda x:_show_pkt(x,terminal))
    else:
        while True:
            a = sniff(count=1,prn=lambda x:_show_pkt(x,terminal))

def _show_pkt(pkt,terminal):
    if terminal == None:
        pkt.summary()
    else:
        terminal.configure(text=terminal.cget("text")+'\n'+str(pkt.summary()))
