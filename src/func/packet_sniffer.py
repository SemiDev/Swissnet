from __future__ import print_function
from scapy.all import *

def sniff_packets(filt,terminal=None):
    try:

        if terminal == None:
            print("[+] Packet Sniffer Started")
            print("[+] Filter: "+filt)
        else:
            terminal.write('\n[+] Packet Sniffer Started\n[+] Filter: '+filt)
        if filt != 'all':
            while True:
                a = sniff(filter=filt,count=1,prn=lambda x:_show_pkt(x,terminal))
        else:
            while True:
                a = sniff(count=1,prn=lambda x:_show_pkt(x,terminal))
    except Exception as s:
        if terminal == None:
            print(s)
        else:
            terminal.write('\n'+str(s))

def _show_pkt(pkt,terminal):
    if terminal == None:
        pkt.summary()
    else:
        terminal.write('\n'+str(pkt.summary()))
