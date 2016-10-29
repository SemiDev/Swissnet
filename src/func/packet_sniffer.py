from __future__ import print_function
from scapy.all import *
import traceback

def sniff_packets(filt,iface,terminal):
    try:
        terminal.write('\n[+] Packet Sniffer Started\n[+] Filter: '+filt)
        if filt != 'all':
            while True:
                a = sniff(filter=filt,iface=iface,count=1,prn=lambda x:_show_pkt(x,terminal))
        else:
            while True:
                a = sniff(count=1,iface=iface,prn=lambda x:_show_pkt(x,terminal))
    except Exception as s:
        terminal.write('\n'+str(s))
        traceback.print_exc()

def _show_pkt(pkt,terminal):
    terminal.write('\n'+str(pkt.summary()))
