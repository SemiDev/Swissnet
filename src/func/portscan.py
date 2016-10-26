import socket

def portscan(ip, maxport, quiet):

    print('-'*40)
    print("[*] WARNING! This method of portscanning is NOT ANNONYMOUS and your ip WILL BE LOGGED on the victim machine.")
    print("-"*40)
    inp = input("Are you SURE you want to continue? y/n\n> ")
    if inp in ("n",'N','no','NO','nO','No'):
        print("[-] Portscan Stopped")
        exit(0)

    openports = []

    s = socket.socket(2,1)
    s.settimeout(0.5)

    print("\n")
    print("// Results For "+ip+" // ")

    if not maxport:
        maxport = 100

    for i in range(int(maxport)+1):
        if quiet:
            try:
                if not s.connect_ex((ip,i)):
                    openports.append(i)
                    print("[+] Open port found: "+str(i))
            except KeyboardInterrupt:
                print("[-] Portscan on "+ip+" stopped")
                break
        else:
            try:
                if not s.connect_ex((ip,i)):
                    openports.append(i)
                    print("[+] Open port found: "+str(i))
                else:
                    print("[-] Port "+str(i)+" is closed")
            except KeyboardInterrupt:
                print("[-] Portscan on "+ip+" stopped")
                break
        
    if not openports:
        print("[-] No open ports found")

    s.close()
