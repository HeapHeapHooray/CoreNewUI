import tkinter as tk
from threading import Thread


tcl = None
tcl_thread = None

def loop_tcl():
    global tcl
    tcl = tk.Tk()
    tcl.withdraw()
    tcl.mainloop()

def is_running():
    global tcl_thread
    return tcl_thread != None

def set_running():
    global tcl
    global tcl_thread
    
    if is_running():
        return

    tcl_thread = Thread(target=loop_tcl,daemon=True)
    tcl_thread.start()
    while tcl == None:
        pass
