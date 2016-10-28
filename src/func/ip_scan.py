import os
import threading
import socket
from func.get_mac import get_mac

def scan_network(verbose,terminal = None):

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
        yn = input("[-] Error: Subnetmask not expected. Do you wish to continue? y/n")
        if yn == 'n' or yn == 'N': 
            exit(1)
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

    print('\n\n // Final Results // \n\n')

    for name,hwaddr,addr in active_ips:
        try:
            if terminal == None:
                print("Name // "+name+" IPv4 // "+addr+' HWAddress // '+hwaddr)
            else:
                terminal.configure(text=terminal.cget("text")+'\nName // '+name+' IPv4 // '+addr+' HWAddress // '+hwaddr)
        except TypeError:
            if terminal == None:
                print("Name // "+name+" IPv4 // "+addr+' HWAddress // '+'unknown')
            else:
                terminal.configure(text=terminal.cget("text")+'\nName // '+name+' IPv4 // '+addr+' HWAddress // unknown')

    return active_ips

def __getips(step,start,quiet,ipr,terminal):
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

                if terminal == None:
                    print("-"*30+"\n"); 
                    print("[+] "+ip+" Is Active ");
                    print("\n"+"-"*30)
                else:
                    terminal.configure(text=terminal.cget("text")+"\n\n[+] "+ip+" Is Active \n")

        elif exitstat and quiet: 
            if terminal == None:
                print("[-] "+ip+" is inavtive ")
            else:
                terminal.configure(text=terminal.cget("text")+'\n[-] '+ip+' is inactive ')
