from __future__ import print_function
import tkinter
import threading
import sys

class mainpage:
    def __init__(self,height,button_width):

        #Defining Extra variables
        self.height = height
        self.button_width = button_width
        self.all_threads = []

    def create_mainpage(self,dospage,poisonpage,scanpage,sniffpage,sessionpage,terminal):
        NUMBER_OF_BUTTONS = 5
        button_height = self.height/NUMBER_OF_BUTTONS

        self.dospage = dospage
        self.poisonpage = poisonpage
        self.scanpage = scanpage
        self.sniffpage = sniffpage
        self.sessionpage = sessionpage

        #Opening Images
        self.dosimage = tkinter.PhotoImage(file='resources/images/dos.png')
        self.poisonimage= tkinter.PhotoImage(file='resources/images/poison.png')
        self.scanimage= tkinter.PhotoImage(file='resources/images/scan.png')
        self.sniffimage= tkinter.PhotoImage(file='resources/images/sniff.png')
        self.sessionimage = tkinter.PhotoImage(file='resources/images/processes.png')

        #Creating Buttons & Text
        self.dos = tkinter.Button(command = lambda: self.dospage.create(self),highlightthickness=0,borderwidth=0,activebackground='#553650',bg='#492f45',image=self.dosimage)
        self.poison = tkinter.Button(command = lambda: self.poisonpage.create(self),highlightthickness=0,borderwidth=0,activebackground='#553650',bg='#492f45',image=self.poisonimage)
        self.scan = tkinter.Button(command = lambda: self.scanpage.create(self),highlightthickness=0,borderwidth=0,activebackground='#553650',bg='#492f45',image=self.scanimage)
        self.sniff = tkinter.Button(command = lambda: self.sniffpage.create(self),highlightthickness=0,borderwidth=0,activebackground='#553650',bg='#492f45',image=self.sniffimage)
        self.sessions = tkinter.Button(command = lambda: self.sessionpage.create_session_page(self,terminal=terminal),highlightthickness=0,borderwidth=0,activebackground='#553650',bg='#492f45',image=self.sessionimage)

        #Placing Buttons & Text
        self.dos.place(x=0,y=0,height=button_height,width=self.button_width)
        self.poison.place(x=0,y=button_height,height=button_height,width=self.button_width)
        self.scan.place(x=0,y=button_height*2,height=button_height,width=self.button_width)
        self.sniff.place(x=0,y=button_height*3,height=button_height,width=self.button_width)
        self.sessions.place(x=0,y=button_height*4,height=button_height,width=self.button_width)

        #Exit Button
        self.exit = tkinter.Button(text="Exit",font=("Helvatica",16),highlightthickness=0,borderwidth=0,activebackground='#553650',bg='#492f45',command=exit)
        self.exit.place(x=700,y=self.height/6*5,height=self.height/6,width=200)

