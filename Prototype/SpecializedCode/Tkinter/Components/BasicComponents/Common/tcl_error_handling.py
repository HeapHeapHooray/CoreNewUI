from tkinter import TclError

class TclErrorHandlingContext:
    def __init__(self):
        pass
    def __enter__(self):
        pass
    def __exit__(self,exception_type,exception_value,exception_traceback):
        if exception_type is TclError:
            print("TclErrorHandlingContext: TclError !")

            raise NotImplemented from TclError
            # Exception was handled succesfully.
            return True
        else:
            return False

def get_tcl_error_handling_context():
    return TclErrorHandlingContext()


# A function decorator that handles TclError.
def handle_tcl_error(func):
    def wrapper_handle_tcl_error(*args,**kwargs):
        try:
            return func(*args,**kwargs)
        except TclError:
            raise NotImplemented from TclError
            #print("TclError !")
    return wrapper_handle_tcl_error
