from scapy.all import *

def get_mac(ip_address):
    responses,unanswered = srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=ip_address),timeout=2,verbose=0)
    for s,r in responses:
        return r[Ether].src

