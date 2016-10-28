import tkinter
from mainpage import mainpage
from create_page import custompage
from terminal import create_terminal

class run_graphical_interface():
    def __init__(self):

        #Creating root
        self.root = tkinter.Tk()
        # self.root.wait_visibility(self.root)
        # self.root.wm_attributes('-alpha',0.9)
        self.root.geometry("900x700")
        self.root.title("Swissnet")
        self.root.configure(bg='#2e1a2b')
        self.root.update()
        self.root.resizable(width=0,height=0)

        #Defining Widget Info
        self.height = self.root.winfo_height()-300
        self.width = self.root.winfo_width()
        self.button_height = int(self.height/4)
        self.button_width = int(self.width/3)

        bannerimage = tkinter.PhotoImage(file='resources/images/banner.png')
        self.banner = tkinter.Label(image=bannerimage,bg='#2e1a2b')
        self.banner.place(x=self.width-450,y=0)

        #Opening Images For Buttons
        #DoS Page [Reflect, SYNFlood, UDPFlood, LANDDoS, PoD]:
        reflectimage = tkinter.PhotoImage(file='resources/images/reflect.png')
        synfloodimage = tkinter.PhotoImage(file='resources/images/synflood.png')
        udpfloodimage = tkinter.PhotoImage(file='resources/images/udpflood.png')
        #landdosimage = tkinter.PhotoImage(file='resources/images/landdos.png')
        #podimage = tkinter.PhotoImage(file='resources/images/pod.png')
        dhcpimage = tkinter.PhotoImage(file='resources/images/dhcpstarvation.png') 

        #Poison Page [ARP Poison, MAC Table Overflow]:
        arppoisonimage = tkinter.PhotoImage(file='resources/images/arppoison.png') 
        mactableoverflowimage = tkinter.PhotoImage(file='resources/images/mactableoverflow.png')

        #Scanners Page [IP Scan, Portscan, Lookup]:
        ipscanimage = tkinter.PhotoImage(file='resources/images/ipscan.png')
        portscanimage = tkinter.PhotoImage(file='resources/images/portscan.png')
        lookupimage = tkinter.PhotoImage(file='resources/images/lookup.png')
        quietscanimage = tkinter.PhotoImage(file='resources/images/quietscan.png') 

        #Sniffers Page [Packet Sniffer]
        packetsnifferimage = tkinter.PhotoImage(file='resources/images/packetsniffer.png')
        ssidsnifferimage = tkinter.PhotoImage(file='resources/images/ssidsniffer.png')

        snifflist = [packetsnifferimage,ssidsnifferimage]


        #Defining lists and IDs for pages:
        doslist = [reflectimage,synfloodimage,udpfloodimage,dhcpimage]
        dosdesc = ["Scans IPs, then performs a reflection attack with scanned ips on a specified VICTIM.",
            "Flood specified VICTIM with TCP SYN requests. Set PORT to 'all' to flood all ports","Flood specifed VICTIM with UDP requests on all ports",
            "Starve your current network of DHCP resources DoSing every client connected"]

        poisonlist = [arppoisonimage,mactableoverflowimage]
        poisondesc = ["Send spoofed ARP packets to VICTIM, so that the VICTIM beleives you are HOST",
            "Overflow a network switch's [VICTIM's] MAC table, causing all traffic to flood out all ports. Use the Packet Sniffer to pick up this traffic"]

        scanlist = [ipscanimage,portscanimage,lookupimage,quietscanimage]
        scandesc = ["Scan for all IPs currentlty on the network. NOTE: This method is fast, but not quiet and your IP will be recorded",
            "Scan ports 1 to MAXPORT of specified VICTIM to see which are open. NOTE: This method is not quiet and your IP will be recorded",
            "Lookup information about HOST",
            "Quietly scan for IPs connected to BSSID by monitoring frames. This way, no packets will be sent. Plus, you do not need to be connnected to the network for this to work"]

        sniffdesc = ["Sniff for incoming Packets and display packet info","Sniff for wireless networks in your area"]

        #Creating Terminal

        self.terminal = create_terminal(self.root.winfo_height()-400,self.height,self.width)

        #Creating Pages:
        self.dos = custompage(self.height,self.button_width,self.width,4,doslist,dosdesc,['reflect','synflood','udpflood','dhcpstarvation'],self.terminal)
        self.poison = custompage(self.height,self.button_width,self.width,2,poisonlist,poisondesc,['arppoison','mactableoverflow'],self.terminal)
        self.scan = custompage(self.height,self.button_width,self.width,4,scanlist,scandesc,['ipscan','portscan','lookup','quietscan'],self.terminal)
        self.sniff = custompage(self.height,self.button_width,self.width,2,snifflist,sniffdesc,['packetsniffer','ssidsniffer'],self.terminal)

        self.main = mainpage(self.height,self.button_width)
        self.main.create_mainpage(self.dos,self.poison,self.scan,self.sniff)

        #Starting Main Window
        self.root.mainloop()
