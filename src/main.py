import signal
import argparse
from command_line import run_command_line
from graphical_user_interface import run_graphical_interface
import threading
import sys
import os
from time import sleep

def signal_handler(signal,frame):
    os.system('sudo airmon-ng stop mon0 > /dev/null')
    print("[-] Program stopped")
    sys.exit()

signal.signal(signal.SIGINT, signal_handler)

def main():

    if os.getuid() == 0:
        print("\n[+] Welcome To Swissnet")
    else:
        print("[-] You must run this program as root")
        sys.exit(0)
        exit()

    ips_been_scanned = False

    parser = argparse.ArgumentParser()
    parser.add_argument('-s','--ipscan',help='Scan for ips on your network',action='store_true')
    parser.add_argument('-p','--portscan',metavar=("IP","MAXPORT"),nargs='*',help='Portscan specified IP with the maximum amount of ports scanned being MAXPORT')
    parser.add_argument('-P','--portscan_ips',help='Portscan scanned ips from --ipscan',action="store_true")
    parser.add_argument('-v','--verbose',action = 'store_true',help='Be verbose when IP scanning and portscanning')
    parser.add_argument("-S","--sniff",nargs=1,metavar="FILTER",help="Sniff for packets on current network with filter FILTER (ex. TCP). Specify FILTER as 'all' to scan for all traffic")
    parser.add_argument("-r","--reflect",metavar="VICTIM",help="Perform reflection attack with scanned ips (--ipscan) on specified victim ALERT: Must be on a big network for this to work")
    parser.add_argument("-syn","--synflood",metavar=("VICTIM","PORT"),nargs=2,help="SYN flood specified VICTIM on PORT. Set PORT to 'all' to flood all ports.")
    parser.add_argument("-u","--udpflood",metavar="VICTIM",nargs=1,help="Perform Denial of Service attack by flooding VICTIM with UDP requests on all ports.")
    parser.add_argument("-L","--landdos",metavar="VICTIM",help="Send a spoofed packet with the same source and destination ip, DoSing the sepcified VICTIM")
    parser.add_argument("-pod","--pingofdeath",metavar="VICTIM",help="Send a malformed ICMP packet ment to glitch out the VICTIM and render them offline")
    parser.add_argument("-o","--mactableoverflow",action='store_true',help="Overflow router's MAC table, sending all traffic out all ports simmilar to a hub. Pick this traffic up with --sniff. Used for Man in the Middle attack (MITM)")
    parser.add_argument("-l","--lookup",metavar="HOST",help="Lookup information about a host IP")
    parser.add_argument("-a","--arppoison",nargs=2,metavar=("TARGET", "HOST"),help="ARP poison TARGET to belive you are HOST")
    parser.add_argument("-d","--dhcpstarvation",action="store_true",help="Starve your current network of it's DHCP resources, DoSing all clients connected to the network")
    parser.add_argument("-D","--deauth",nargs=3,metavar=("BSSID","VICTIM_MAC","IFACE"),help="Send 802.11 deauthentication packets to VICTIM on network BSSID on interface IFACE")
    parser.add_argument("-n","--nestea",metavar=("VICTIM"),help="A classic packet fragmentation error that crashes some versions of windows under Windows XP")
    parser.add_argument("-c","--commandline",action="store_true",help="\nProgram wont use a graphic interface, but will instead be a command line program.\n")
    args = parser.parse_args()

    if args.commandline:
        print('[+] Running Command Line')
        run_command_line(args)
    else:
        run_graphical_interface()

if __name__ == '__main__':
    main()
