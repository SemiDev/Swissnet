import tkinter

class create_terminal:
    def __init__(self,root,height,bodyheight,width):
        welcomemsg = '\n[+] Welcome To Swissnet\n[+] All output from the swissnet tools will appear here\n[+] Note: Use the "-c" option to use Swissnet in command line mode\n'

        self.terminal = tkinter.Text(root,font=('Helvatica',10),highlightthickness=0,
        borderwidth=0,bg='#251b25',height=20,width=400)

        scrollbar = tkinter.Scrollbar(root,width=10)

        self.terminal.configure(yscrollcommand=scrollbar.set)
        self.terminal.insert(tkinter.END,welcomemsg)
        self.terminal.place(x=0,y=bodyheight)

        self.terminal.config(state='disabled')

        scrollbar.config(command=self.terminal.yview)
        scrollbar.place(x=width-10,y=bodyheight,height=height)

    def write(self,string):
        self.terminal.config(state='normal')
        self.terminal.insert(tkinter.END,string)
        self.terminal.config(state='disabled')
