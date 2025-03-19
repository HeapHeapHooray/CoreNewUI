import tkinter
from .Base import SimpleBasicComponent
from .Common import handle_tcl_error
from PIL import ImageTk


class Label(SimpleBasicComponent):
    def __init__(self,parent):
        super().__init__(parent,tkinter.Label)
    @handle_tcl_error
    def set_text(self,text: str):
        self._native_basic_component.config(text = text)
    @handle_tcl_error
    def set_image(self,image: ImageTk):
        self._native_basic_component.config(image = image)
    @handle_tcl_error
    def set_background_color(self,color: str):
        self._native_basic_component.config(bg=color)
    
