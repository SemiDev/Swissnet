from functools import partial
import tkinter
from func.portscan import portscan
from func.ip_scan import scan_network
from func.packet_sniffer import sniff_packets
from func.reflection import reflection
from func.arpspoof import arpspoof
from func.SYNflood import SYNflood
from func.LANDDoS import LANDDoS
from func.UDPflood import UDPflood
from func.lookup import lookup
from func.ping_of_death import ping_of_death
from func.mactableoverflow import mactableoverflow
from func.DHCPstarvation import DHCPstarvation
from func.quietscan import quietscan

THREAD_COUNT = 300

class custompage:
    def __init__(self,height,button_width,width,NOB,imagelist,desclist = [],buttonlist=[]):
        #Defining Extra variables
        self.height = height
        self.button_width = button_width
        self.width = width
        self.all_buttons = []
        self.imagelist = imagelist
        self.globaldesc = None
        self.desclist = desclist
        self.buttonlist=buttonlist
        self.NUMBER_OF_BUTTONS = NOB 
        self.all_extra = []
        self.run_image = tkinter.PhotoImage(file='resources/images/run.png')

    def create(self,mainpage):

        button_height = self.height/self.NUMBER_OF_BUTTONS
        self.mainpage = mainpage

        goback_image = tkinter.PhotoImage(file='resources/images/gobackbutton.png')
        self.gobackbutton = tkinter.Button(text="Go Back",font=("Helvatica",16),highlightthickness=0,borderwidth=0,activebackground='#553650',bg='#492f45',command=self.hide)
        self.gobackbutton.place(x=self.width-200,y=self.height/6*5,height=self.height/6,width=200)

        #Creating Buttons & Text
        for i in range(self.NUMBER_OF_BUTTONS):
            button_object = tkinter.Button(command=partial(self.options, self.desclist[i-1],self.buttonlist[i-1]),highlightthickness=0,borderwidth=0,activebackground='#553650',bg='#492f45',image=self.imagelist[i-1])
            self.all_buttons.append(button_object)

        #Placing Buttons & Tect
        for i, b in enumerate(self.all_buttons):
            b.place(x=0,y=button_height*i-1,height=button_height,width=self.button_width)

    def hide(self):
        for b in self.all_buttons:
            b.destroy()

        for object in self.all_extra:
            object.destroy()

        self.all_buttons = []
        try:
            self.globaldesc.destroy()
        except AttributeError:
            pass

        self.gobackbutton.destroy()

    def options(self,desc,id):

        for object in self.all_extra:
            object.destroy()

        try: 
            self.globaldesc.destroy()
        except AttributeError:
            pass
            
        description = tkinter.Label(text=desc,bg='#2e1a2b',wraplength=285,justify='right',font=("resources/fonts/trench100free",12))
        description.place(x=610,y=150)
        self.globaldesc = description
    
        if id not in ["quietscan","dhcpstarvation","portscan","arppoison","ipscan","lookup","mactableoverflow","synflood","packetsniffer"]:
            textinput = self.__create_base_layout(1,"Victim")
            self.__runbutton(partial(self._do_command,id,textinput))
        elif id == "packetsniffer":
            textinput = self.__create_base_layout(1,"Filter")
            self.__runbutton(partial(self._do_command,id,textinput))
        elif id == "quietscan":
            textinput = self.__create_base_layout(1,"BSSID")
            self.__runbutton(partial(self._do_command,id,textinput))
        elif id == "lookup":
            textinput = self.__create_base_layout(1,"Host")
            self.__runbutton(partial(self._do_command,id,textinput))
        elif id == "dnslookup":
            textinput = self.__create_base_layout(1,"Host")
            self.__runbutton(partial(self._do_command,id,textinput))
        elif id == "synflood":
            textinput = self.__create_base_layout(2,("Victim","Port"))
            self.__runbutton(partial(self._do_command,id,textinput))
        elif id == "arppoison":
            textinput = self.__create_base_layout(2,("Victim","Host"))
            self.__runbutton(partial(self._do_command,id,textinput))
        elif id in ["ipscan","mactableoverflow","dhcpstarvation"]:
            textinput = self.__create_base_layout(0,"")
            self.__runbutton(partial(self._do_command,id,textinput))
        elif id == 'portscan':
            textinput = self.__create_base_layout(2,("Victim","MaxPort"))
            self.__runbutton(partial(self._do_command,id,textinput))

    def __create_base_layout(self,nargs,text):

        if nargs==1:
            label = tkinter.Button(text=text,font=('Helvatica',14),highlightthickness=0,borderwidth=0,activebackground='#492f45',bg='#492f45')        
            label.place(x = self.button_width+20,y=250)

            textinput = tkinter.Entry(width=12,bg='#886883',highlightthickness=0,borderwidth=0,font=('Arial'))
            textinput.place(x=self.button_width+120,y=255)

            self.all_extra.append(textinput)
            self.all_extra.append(label)

            return textinput

        elif nargs==2:
            label = tkinter.Button(text=text[0],font=('Helvatica',14),highlightthickness=0,borderwidth=0,activebackground='#492f45',bg='#492f45')        
            label.place(x = self.button_width+20,y=230)

            label2 = tkinter.Button(text=text[1],font=('Helvatica',14),highlightthickness=0,borderwidth=0,activebackground='#492f45',bg='#492f45')        
            label2.place(x = self.button_width+20,y=270)

            textinput = tkinter.Entry(width=12,bg='#886883',highlightthickness=0,borderwidth=0,font=('Arial'))
            textinput.place(x=self.button_width+120,y=235)

            textinput2 = tkinter.Entry(width=12,bg='#886883',highlightthickness=0,borderwidth=0,font=('Arial'))
            textinput2.place(x=self.button_width+120,y=275)

            self.all_extra.append(textinput)
            self.all_extra.append(textinput2)
            self.all_extra.append(label)
            self.all_extra.append(label2)

            return (textinput,textinput2)

    def __do_reflection(self,victim):
        active_ips = scan_network(False)
        reflection(victim,active_ips)
    
    def __runbutton(self,command):
            self.run_button = tkinter.Button(command=command,image=self.run_image,highlightthickness=0,borderwidth=0,activebackground='#553650',bg='#492f45')        
            self.run_button.place(x=self.button_width,y=self.height/6*5,height=self.height/6,width=200)
            self.all_extra.append(self.run_button)

    def _do_command(self,id,textinput):
        if id == 'reflect':
            input = textinput.get()
            self.__do_reflection(input)
        elif id == 'udpflood':
            input = textinput.get()
            UDPflood(input,True,THREAD_COUNT)
        elif id == 'synflood':
            input1 = textinput[0].get()
            input2 = textinput[1].get() 
            SYNflood(input1,input2,True,THREAD_COUNT)
        elif id == 'arppoison':
            input1 = textinput[0].get()
            input2 = textinput[1].get() 
            arpspoof(input1,input2)
        elif id == 'arppoison':
            input = textinput.get()
            arpspoof(input,True)
        elif id == 'mactableoverflow':
            mactableoverflow(THREAD_COUNT,True)
        elif id == 'lookup':
            input = textinput.get()
            lookup(input)
        elif id == 'ipscan':
            scan_network(False)
        elif id == 'portscan':
            input = textinput[0].get()
            input2 = textinput[1].get()
            portscan(input,input2,True)
        elif id == 'packetsniffer':
            inp = textinput.get()
            sniff_packets(inp)
        elif id == 'dhcpstarvation':
            DHCPstarvation()
        elif id == 'quietscan':
            input = textinput.get()
            quietscan(input)
