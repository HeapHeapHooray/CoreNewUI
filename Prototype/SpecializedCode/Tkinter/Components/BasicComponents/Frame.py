import tkinter
from .Base import SimpleBasicComponent
from .Common import handle_tcl_error

class Frame(SimpleBasicComponent):
    def __init__(self,parent):
        super().__init__(parent,tkinter.Frame)
    @handle_tcl_error
    def set_pack_propagation(self,should_propagate: bool):
        propagation_flag = 0
        if should_propagate:
            propagation_flag = 1
        self._native_basic_component.pack_propagate(propagation_flag)
    @handle_tcl_error
    def place(self,**args):
        self._native_basic_component.place(**args)
    @handle_tcl_error
    def set_background_color(self,color: str):
        self._native_basic_component.config(bg=color)
        
