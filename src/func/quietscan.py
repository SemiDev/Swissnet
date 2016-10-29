from scapy.all import *
import os

active_ips = []
bssid = '' 

def quietscan(networkmac,trm=None):

    global terminal
    terminal = trm

    os.system('sudo airmon-ng start wlan0 > /dev/null') 

    global bssid
    bssid = networkmac
    
    if terminal == None:
        print('[+] Monitoring for activity on '+bssid)
    else:
        terminal.write('\n[+] Monitoring fot activity on '+bssid)

    sniff(iface='mon0',prn=_filter_packet)

def _filter_packet(pkt):
    try:
        if pkt.haslayer(Dot11):
            if pkt.addr3 == bssid:
                if pkt.addr2 not in active_ips:
                    active_ips.append(pkt.addr2)
                    try:
                        if terminal == None:
                            print('[+] HWAddress // '+pkt.addr2+' BSSID // '+pkt.addr3)
                        else:
                            terminal.write('\n[+] HWAddress // '+pkt.addr2+' BSSID // '+pkt.addr3)
                    except:
                        pass
    except Exception as s:
        if terminal == None:
            print(s)
        else:
            terminal.write('\n'+str(s))
