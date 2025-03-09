import tkinter
from .Base import SimpleBasicComponent
from .Common import handle_tcl_error

class Toplevel(SimpleBasicComponent):
    def __init__(self):
        super().__init__(None,tkinter.Toplevel)
    @handle_tcl_error
    def set_pack_propagation(self,should_propagate: bool):
        propagation_flag = 0
        if should_propagate:
            propagation_flag = 1
        self._native_basic_component.pack_propagate(propagation_flag)
    @handle_tcl_error
    def set_background_color(self,color: str):
        self._native_basic_component.configure(bg = color)
    
        
