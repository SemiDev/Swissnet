import socket

def portscan(ip, maxport, quiet,terminal=None):
    try:
        if terminal == None:
            print('-'*40)
            print("[*] WARNING! This method of portscanning is NOT ANNONYMOUS and your ip WILL BE LOGGED on the victim machine.")
            print("-"*40)
            inp = input("Are you SURE you want to continue? y/n\n> ")
            if inp in ("n",'N','no','NO','nO','No'):
                print("[-] Portscan Stopped")
                exit(0)
        else:
            terminal.write('\n[*] WARNING: This method of portscanning is NOT ANNONYMOUS and yout ip WILL BE LOGGED on the victim machine.')

        openports = []

        s = socket.socket(2,1)
        s.settimeout(0.5)

        if terminal == None:
            print("\n")
            print("// Results For "+ip+" // ")
        else:
            terminal.write('\n\n//Results For '+ip+' // ')

        if not maxport:
            maxport = 100

        for i in range(int(maxport)+1):
            if quiet:
                try:
                    if not s.connect_ex((ip,i)):
                        openports.append(i)
                        if terminal == None:
                            print("[+] Open port found: "+str(i))
                        else:
                            terminal.write('\n[+] Open port found: '+str(i))
                except:
                    pass
            else:
                try:
                    if not s.connect_ex((ip,i)):
                        openports.append(i)
                        if terminal == None:
                            print("[+] Open port found: "+str(i))
                        else:
                            terminal.write('\n[+] Open port found '+str(i))
                    else:
                        if terminal == None:
                            print("[-] Port "+str(i)+" is closed")
                        else:
                            terminal.write('\n[-] Port '+str(i)+' is closed ')

                except:
                    pass
            
        if not openports:
            if terminal == None:
                print("[-] No open ports found")
            else:
                terminal.write('\n[-] No open ports found')

        s.close()
    except Exception as s:
        if terminal == None:
            print(s)
        else:
            terminal.write('\n'+str(s))
