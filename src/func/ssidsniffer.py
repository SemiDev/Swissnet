from __future__ import print_function
from scapy.all import *
import os

all_ssids = []

def ssidsniffer(terminal = None):
    try:
        term = terminal

        if terminal == None:
            print('[+] Sniffing for wireless SSIDs')
        else:
            terminal.write('\n[+] Sniffing for wireless SSIDs')

        os.system('sudo airmon-ng start wlan0 > /dev/null')
        sniff(iface='mon0',prn= lambda x:_parse_pkt(x,terminal))

    except Exception as s:
        if terminal == None:
            print(s)
        else:
            terminal.write('\n'+str(s))

def _parse_pkt(pkt,terminal):
    try:
        if pkt.haslayer(Dot11):
            try:
                ssid = pkt[0].info.decode()
                if ssid not in all_ssids:
                    all_ssids.append(ssid)
                    bssid = pkt[0].addr3
                    channel = str(ord(pkt[0][Dot11Elt:3].info))
                    if terminal == None:
                        print('[+] BSSID // '+bssid+' | SSID '+ssid+' | Channel // '+channel)
                    else:
                        terminal.write('\n[+] BSSID // '+bssid+' | SSID '+ssid+' | Channel // '+channel)
            except AttributeError:
                pass
    except Exception as s:
        if terminal == None:
            print(s)
        else:
            terminal.write('\n'+str(s))
            
        
        
