import socket
import traceback
import time

def portscan(ip, maxport, quiet,terminal):
    try:
        terminal.write('\n[*] WARNING: This method of portscanning is NOT ANNONYMOUS and yout ip WILL BE LOGGED on the victim machine.')
        time.sleep(2)

        openports = []

        s = socket.socket(2,1)
        s.settimeout(0.5)

        terminal.write('\n\n//Results For '+ip+' // ')

        if not maxport:
            maxport = 100

        for i in range(int(maxport)+1):
            if quiet:
                try:
                    if not s.connect_ex((ip,i)):
                        openports.append(i)
                        terminal.write('\n[+] Open port found: '+str(i))
                except:
                    pass
            else:
                try:
                    if not s.connect_ex((ip,i)):
                        openports.append(i)
                        terminal.write('\n[+] Open port found '+str(i))
                    else:
                        terminal.write('\n[-] Port '+str(i)+' is closed ')

                except:
                    pass

        if not openports:
            terminal.write('\n[-] No open ports found')

        s.close()
    except Exception as s:
        terminal.write('\n'+str(s))
        traceback.print_exc()
