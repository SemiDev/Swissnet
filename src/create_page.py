from functools import partial
from threading import Thread
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
from func.ssidsniffer import ssidsniffer

THREAD_COUNT = 300

class custompage:
    #NOB: Number of buttons
    def __init__(self,height,button_width,width,NOB,imagelist,desclist = [],buttonlist=[],terminal=None):
        #Defining Extra variables
        self.terminal = terminal
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

    def create_session_page(self,mainpage,terminal):
        self.stop_image = tkinter.PhotoImage(file='resources/images/stop.png')
        self.session_buttons = []

        NUMBER_OF_BUTTONS = len(mainpage.all_threads)
        try:
            button_height = self.height/NUMBER_OF_BUTTONS
        except ZeroDivisionError:
            terminal.write('\n\n[+] There are currently no processes running\n')

        goback_image = tkinter.PhotoImage(file='resources/images/gobackbutton.png')
        self.Sgobackbutton = tkinter.Button(text="Go Back",font=("Helvatica",16),highlightthickness=0,borderwidth=0,activebackground='#553650',bg='#492f45',command=self.hide)
        self.Sgobackbutton.place(x=self.width-200,y=self.height/6*5,height=self.height/6,width=200)

        for n,(id,t) in enumerate(mainpage.all_threads):
            b = tkinter.Button(command=partial(self.session_base_layout,t,id,terminal,mainpage),highlightthickness=0,
            borderwidth=0,activebackground='#553650',bg='#492f45',text=id,font=('Helvetica',17))
            b.place(x=0,y=button_height*n-1,height=button_height,width=self.button_width)
            self.all_buttons.append(b)

    def session_base_layout(self,t,id,terminal,mainpage):

        for object in self.session_buttons:
            object.destroy()
        for object in self.all_extra:
            object.destroy()

        self.stop_button = tkinter.Button(command=partial(self._stop_process,t,id,terminal,mainpage),image=self.stop_image,highlightthickness=0,borderwidth=0,activebackground='#553650',bg='#492f45')        
        self.stop_button.place(x=self.button_width,y=self.height/6*5,height=self.height/6,width=200)
        self.all_extra.append(self.stop_button)

    def _stop_process(self,t,id,terminal,mainpage):
        mainpage.all_threads.remove((id,t))
        terminal.write('\n\n[*] Process '+id+' successfully stopped')
        self.hide()

    def create(self,mainpage):

        button_height = self.height/self.NUMBER_OF_BUTTONS 
        self.mainpage = mainpage

        goback_image = tkinter.PhotoImage(file='resources/images/gobackbutton.png')
        self.gobackbutton = tkinter.Button(text="Go Back",font=("Helvatica",16),highlightthickness=0,borderwidth=0,activebackground='#553650',bg='#492f45',command=self.hide)
        self.gobackbutton.place(x=self.width-200,y=self.height/6*5,height=self.height/6,width=200)

        #Creating Buttons & Text
        for i in range(self.NUMBER_OF_BUTTONS):
            button_object = tkinter.Button(command=partial(self.options, self.desclist[i-1],self.buttonlist[i-1],mainpage),highlightthickness=0,borderwidth=0,activebackground='#553650',bg='#492f45',image=self.imagelist[i-1])
            self.all_buttons.append(button_object)

        #Placing Buttons & Text
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

        try:
            self.gobackbutton.destroy()
        except AttributeError:
            pass

        try:
            self.Sgobackbutton.destroy()
        except AttributeError:
            pass

    def options(self,desc,id,mainpage):

        for object in self.all_extra:
            object.destroy()

        try: 
            self.globaldesc.destroy()
        except AttributeError:
            pass
            
        description = tkinter.Label(text=desc,bg='#2e1a2b',wraplength=285,justify='right',font=("resources/fonts/trench100free",12))
        description.place(x=610,y=150)
        self.globaldesc = description
    
        if id not in ["ssidsniffer","quietscan","dhcpstarvation","portscan","arppoison","ipscan","lookup","mactableoverflow","synflood","packetsniffer"]:
            textinput = self.__create_base_layout(1,"Victim")
            self.__runbutton(partial(self._do_command,id,textinput,mainpage))
        elif id == "packetsniffer":
            textinput = self.__create_base_layout(1,"Filter")
            self.__runbutton(partial(self._do_command,id,textinput,mainpage))
        elif id == 'ssidsniffer':
            textinput = self.__create_base_layout(0,'')
            self.__runbutton(partial(self._do_command,id,textinput,mainpage))
        elif id == "quietscan":
            textinput = self.__create_base_layout(1,"BSSID")
            self.__runbutton(partial(self._do_command,id,textinput,mainpage))
        elif id == "lookup":
            textinput = self.__create_base_layout(1,"Host")
            self.__runbutton(partial(self._do_command,id,textinput,mainpage))
        elif id == "dnslookup":
            textinput = self.__create_base_layout(1,"Host")
            self.__runbutton(partial(self._do_command,id,textinput,mainpage))
        elif id == "synflood":
            textinput = self.__create_base_layout(2,("Victim","Port"))
            self.__runbutton(partial(self._do_command,id,textinput,mainpage))
        elif id == "arppoison":
            textinput = self.__create_base_layout(2,("Victim","Host"))
            self.__runbutton(partial(self._do_command,id,textinput,mainpage))
        elif id in ["ipscan","mactableoverflow","dhcpstarvation"]:
            textinput = self.__create_base_layout(0,"")
            self.__runbutton(partial(self._do_command,id,textinput,mainpage))
        elif id == 'portscan':
            textinput = self.__create_base_layout(2,("Victim","MaxPort"))
            self.__runbutton(partial(self._do_command,id,textinput,mainpage))

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

    def __do_reflection(self,victim,terminal = None):
        active_ips = scan_network(False,terminal = terminal)
        terminal.configure(text=terminal.cget('text') + '\n [+] Scanning for IPs on the network...')
        t = Thread(target=reflection,args=(victim,active_ips),kwargs={'terminal' : terminal})
        t.daemon = True
        t.start()
    
    def __runbutton(self,command):
            self.run_button = tkinter.Button(command=command,image=self.run_image,highlightthickness=0,borderwidth=0,activebackground='#553650',bg='#492f45')        
            self.run_button.place(x=self.button_width,y=self.height/6*5,height=self.height/6,width=200)
            self.all_extra.append(self.run_button)

    def _do_command(self,id,textinput,mainpage):
        if id == 'reflect':
            input = textinput.get()
            self.__do_reflection(input,terminal=self.terminal)
        elif id == 'udpflood':
            input = textinput.get()
            t = Thread(target=UDPflood,args=(input,True,THREAD_COUNT),kwargs={'terminal':self.terminal})
        elif id == 'synflood':
            input1 = textinput[0].get()
            input2 = textinput[1].get() 
            t = Thread(target=SYNflood,args=(input1,input2,True,THREAD_COUNT),kwargs={'terminal':self.terminal})
        elif id == 'arppoison':
            input1 = textinput[0].get()
            input2 = textinput[1].get() 
            t = Thread(target=arpspoof, args=(input1,input2), kwargs={'terminal' : self.terminal})
        elif id == 'mactableoverflow':
            t = Thread(target=mactableoverflow,args=(THREAD_COUNT,True),kwargs={'terminal' : self.terminal})
        elif id == 'lookup':
            input = textinput.get()
            t = Thread(target=lookup,args=(input,),kwargs={'terminal' : self.terminal})
        elif id == 'ipscan':
           t = Thread(target=scan_network,args=(False,),kwargs={'terminal' : self.terminal})
        elif id == 'portscan':
            input = textinput[0].get()
            input2 = textinput[1].get()
            t = Thread(target=portscan,args=(input,input2,True),kwargs={'terminal' : self.terminal})
        elif id == 'packetsniffer':
            inp = textinput.get()
            t = Thread(target=sniff_packets,args=(inp,),kwargs={'terminal' : self.terminal})
        elif id == 'dhcpstarvation':
            t = Thread(target=DHCPstarvation,kwargs={'terminal' : self.terminal})
        elif id == 'quietscan':
            input = textinput.get()
            t = Thread(target=quietscan,args=(input),kwargs={'terminal' : self.terminal})
        elif id == 'ssidsniffer':
            t = Thread(target=ssidsniffer,kwargs={'terminal' : self.terminal})

        t.daemon=True
        t.start()
        mainpage.all_threads.append((id,t))
