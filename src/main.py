import signal
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
    run_graphical_interface()

if __name__ == '__main__':
    main()
