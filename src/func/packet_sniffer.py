from scapy.all import *

def sniff_packets(filt):
    print("[+] Packet Sniffer Started")
    print("[+] Filter: "+filt)
    if filt != 'all':
        while True:
            a = sniff(filter=filt,count=1,prn=lambda x: x.summary())
    else:
        while True:
            a = sniff(count=1,prn=lambda x: x.summary())