from struct import *
from func.portscan import portscan
from func.ip_scan import scan_network
from func.packet_sniffer import sniff_packets
from func.reflection import reflection
from func.arpspoof import arpspoof
from func.SYNflood import SYNflood
from func.LANDDoS import LANDDoS
from func.UDPflood import UDPflood
from func.lookup import lookup
from func.ping_of_death import ping_of_death
from func.mactableoverflow import mactableoverflow
from func.nestea import nestea
from func.DHCPstarvation import DHCPstarvation

def run_command_line(args):

    ip_range = ''
    all_threads = []
    verbose = False
    THREAD_COUNT = 300

    if args.verbose:
        verbose = False
    elif not args.verbose:
        verbose = True

    if args.sniff:
        sniff_packets(args.sniff[0])

    if args.ipscan:
        active_ips = scan_network(args.verbose)
        ips_been_scanned = True
        if args.portscan_ips:
            for name, hwaddr, addr in active_ips:
                portscan(addr,0,verbose)
        if args.reflect:
            reflection(args.reflect,active_ips)

    if args.lookup:
        lookup(args.lookup)

    if args.udpflood:
        UDPflood(args.udpflood,verbose,THREAD_COUNT)

    ap = args.arppoison
    if ap:
        arpspoof(ap[0],ap[1])

    if args.portscan:
        try:
            portscan(args.portscan[0],args.portscan[1],verbose)
        except IndexError:
            portscan(args.portscan[0],0,verbose)

    if args.landdos:
        LANDDoS(args.landdos[0],verbose)

    if args.synflood:
        SYNflood(args.synflood[0],args.synflood[1],verbose,THREAD_COUNT)
        

    if args.portscan_ips and not ips_been_scanned:
        print("[-] Error: You must scan the networks IPs before using this option. Try swissnet -sP")

    if args.reflect and not ips_been_scanned:
        print("[-] Error: You must scan the networks IPs before using this option. Try swissnet -sr VICTIM")

    if args.pingofdeath:
        ping_of_death(args.pingofdeath,verbose)

    if args.mactableoverflow:
        mactableoverflow(THREAD_COUNT,verbose) 

    if args.dhcpstarvation: 
        DHCPstarvation() 

    if args.deauth:
        deauth(args.deauth[0],args.deauth[1],args.deauth[2])
    
    if args.nestea:
        nestea(args.nestea)
