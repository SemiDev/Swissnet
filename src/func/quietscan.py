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
        terminal.configure(text=terminal.cget("text")+'\n[+] Monitoring fot activity on '+bssid)

    sniff(iface='mon0',prn=_filter_packet)

def _filter_packet(pkt):
    if pkt.haslayer(Dot11):
        if pkt.addr3 == bssid:
            if pkt.addr2 not in active_ips:
                active_ips.append(pkt.addr2)
                try:
                    if terminal == None:
                        print('[+] HWAddress // '+pkt.addr2+' BSSID // '+pkt.addr3)
                    else:
                        terminal.configure(text=terminal.cget("text")+'\n[+] HWAddress // '+pkt.addr2+' BSSID // '+pkt.addr3)
                except:
                    pass

if __name__ == '__main__':
    quietscan('84:a4:23:8d:c6:30')
