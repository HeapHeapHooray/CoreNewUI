import tkinter
from .Base import TkinterBasicComponent

class Label(TkinterBasicComponent):
    def __init__(self):
        super().__init__()
    def _create_basic_component(self):
        if self._parent == None:
            return
        print("Creating Basic Component...")
        native_parent_basic_component = self._parent.get_root_native_basic_component()
        self._native_basic_component = tkinter.Label(native_parent_basic_component)
        self._native_basic_component.config(text = "Test")
        self._native_basic_component.pack(fill=tkinter.BOTH,expand=1)
    def _destroy_basic_component(self):
        if self._native_basic_component == None:
            return
        self._native_basic_component.destroy()
