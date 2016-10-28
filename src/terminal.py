import tkinter

def create_terminal(height,bodyheight,width):
    welcomemsg = '\n[+] Welcome To Swissnet\n[+] All output from the swissnet tools will appear here\n[+] Note: Use the "-c" option to use Swissnet in command line mode\n'
    terminal = tkinter.Label(text=welcomemsg,font=('Helvatica',10),highlightthickness=0,
        borderwidth=0,bg='#251b25',anchor='nw',justify='left',height=20,width=400)
    terminal.place(x=0,y=bodyheight)
    return terminal
