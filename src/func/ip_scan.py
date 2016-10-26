import os
import threading
import socket

def scan_network(verbose):

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

    tc = 150

    for i in range(tc):
        ip = threading.Thread(target=__getips,args=(tc,i,verbose,ipr))
        ip.daemon = True
        ip.start()
        all_threads.append(ip)
        i+=1

    for thread in all_threads:
        thread.join()

    print('\n\n // Final Results // \n\n')

    for name,alias,addr in active_ips:
        print("Name: "+name+" IPv4: "+addr[0])

    return active_ips

def __getips(step,start,quiet,ipr):
    for i in range(start,255,step):
        ip = ipr % i
        exitstat = os.system('fping -q -t 50 '+ip)
        if not exitstat:
            try:
                name, alias, addr = socket.gethostbyaddr(ip)
                active_ips.append((name,alias,addr))
            except:
                active_ips.append(('unknown','unknown',[ip]))
            finally:
                print("-"*30+"\n"); print("[+] "+ip+" Is Active ");print("\n"+"-"*30)
        elif exitstat and quiet: 
            print("[-] "+ip+" is inavtive ")
