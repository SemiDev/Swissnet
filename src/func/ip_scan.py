import os
import threading
import socket
from func.get_mac import get_mac
import traceback

def scan_network(verbose,terminal):
    try:

        all_threads = []
        global active_ips
        active_ips = []

        subnetmask = os.popen("ifconfig wlan0 | grep Mask: | awk '{print $4}'").read()[5:]

        ipr = os.popen("ip route show | grep -i 'default via'| awk '{print $3 }'").read()
        ipr = ipr.strip()

        if subnetmask.strip() == '255.255.255.0':
            ipr = ipr.split(".")
            ipr = ipr[0] +"."+ ipr[1] +"."+ ipr[2] + "."+"%d"
        else:
            terminal.write('\n[-] Error: Subnetmask not expected. This program will only scan a portion of the IPs currently on the network')
            ipr = ipr.split(".")
            ipr = ipr[0] +"."+ ipr[1] +"."+ ipr[2] + "."+"%d"

        tc = 150

        for i in range(tc):
            ip = threading.Thread(target=__getips,args=(tc,i,verbose,ipr,terminal))
            ip.daemon = True
            ip.start()
            all_threads.append(ip)
            i+=1

        for thread in all_threads:
            thread.join()

        terminal.write('\n\n // Final Results // \n\n')

        for name,hwaddr,addr in active_ips:
            try:
                terminal.write('\nName // '+name+' IPv4 // '+addr+' HWAddress // '+hwaddr)
            except TypeError:
                terminal.write('\nName // '+name+' IPv4 // '+addr+' HWAddress // unknown')

        return active_ips
    except Exception as s:
        terminal.write('\n'+str(s))
        traceback.print_exc()
def __getips(step,start,quiet,ipr,terminal):
    try:
        for i in range(start,255,step):
            ip = ipr % i
            exitstat = os.system('fping -q -t 50 '+ip)
            if not exitstat:
                tmp = []
                try:
                    name, alias, addr = socket.gethostbyaddr(ip)
                    tmp.append(name)
                except:
                    tmp.append('unknown')
                finally:
                    tmp.append(get_mac(ip))
                    tmp.append(ip)
                    active_ips.append(tuple(tmp))

                    terminal.write("\n\n[+] "+ip+" Is Active \n")

            elif exitstat and quiet:
                terminal.write('\n[-] '+ip+' is inactive ')
    except Exception as s:
        terminal.write('\n'+str(s))
        traceback.print_exc()
