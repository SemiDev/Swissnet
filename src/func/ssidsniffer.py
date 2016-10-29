from __future__ import print_function
from scapy.all import *
import os
import traceback

all_ssids = []

def ssidsniffer(terminal):
    try:
        term = terminal

        terminal.write('\n[+] Sniffing for wireless SSIDs')

        os.system('sudo airmon-ng start wlan0 > /dev/null')
        sniff(iface='mon0',prn= lambda x:_parse_pkt(x,terminal))

    except Exception as s:
        terminal.write('\n'+str(s))
        traceback.print_exc()

def _parse_pkt(pkt,terminal):
    try:
        if pkt.haslayer(Dot11):
            try:
                ssid = pkt[0].info.decode()
                if ssid not in all_ssids:
                    all_ssids.append(ssid)
                    bssid = pkt[0].addr3
                    channel = str(ord(pkt[0][Dot11Elt:3].info))
                    terminal.write('\n[+] BSSID // '+bssid+' | SSID '+ssid+' | Channel // '+channel)
            except AttributeError:
                pass
    except Exception as s:
        terminal.write('\n'+str(s))
        traceback.print_exc()
