''' Incase you wish to create your own module, here's an example
of things required for the app to work'''

#You MUST import traceback for error handling
import traceback

#Create custom function with arg 'terminal'.
#This will be important later
def my_function(terminal):
    #Encapsulate the entire function in a try except statement so that we can print errors to screen
    try:
        do_something()
        #This is very important if you want to print something to screen
        #Printing to GUI
        #NOTE: The write function does not come with a built in newline like print does, so you have to add that yourself
        terminal.write('\n[+] Printing to built in screen in GUI')

    #Here's the 'except' part to the try-except
    #This is so that any errors can print to the GUI screen as well

    except Exception:
        #Printing to GUI
        #Remember, the terminal does not have a built-in newline function, so you have to add that your self
        terminal.write('\n'+str(s))
        traceback.print_exc()
