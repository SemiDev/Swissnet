from __future__ import print_function
from scapy.all import *
import os

all_ssids = []

def ssidsniffer(terminal = None):
    term = terminal
    os.system('sudo airmon-ng start wlan0 > /dev/null')

    if terminal == None:
        print('[+] Sniffing for wireless SSIDs')
    else:
        terminal.configure(text=terminal.cget('text')+'[+] Sniffing for wireless SSIDs')

    sniff(iface='mon0',prn= lambda x:_parse_pkt(x,terminal))

def _parse_pkt(pkt,terminal):
    if pkt.haslayer(Dot11):
        ssid = pkt[0].info.decode()
        if pkt not in all_ssids:
            all_ssids.append(ssid)
            bssid = pkt[0].addr3
            channel = str(ord(pkt[0][Dot11Elt:3].info))
            if terminal == None:
                print('[+] BSSID // '+bssid+' | SSID '+ssid+' | Channel // '+channel)
            else:
                terminal.configure(text=terminal.cget('text')+'\n[+] BSSID // '+bssid+' | SSID '+ssid+' | Channel // '+channel)
        
        
