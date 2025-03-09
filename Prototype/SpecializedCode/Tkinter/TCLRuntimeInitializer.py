from ...TkinterRuntime import TCLRuntime

class TCLRuntimeInitializer:
    def __init__(self):
        if not TCLRuntime.is_running():
            print("Initializing TCL Runtime...")
            TCLRuntime.set_running()
