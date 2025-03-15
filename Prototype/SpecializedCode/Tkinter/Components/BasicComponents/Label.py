import tkinter
from .Base import SimpleBasicComponent
from .Common import handle_tcl_error

class Label(SimpleBasicComponent):
    def __init__(self,parent):
        super().__init__(parent,tkinter.Label)
    @handle_tcl_error
    def set_text(self,text: str):
        self._native_basic_component.config(text = text)
    @handle_tcl_error
    def pack(self):
        self._native_basic_component.pack(fill=tkinter.BOTH,expand=1)
    @handle_tcl_error
    def place(self,**args):
        self._native_basic_component.place(**args)
    @handle_tcl_error
    def set_background_color(self,color: str):
        self._native_basic_component.config(bg=color)
    
