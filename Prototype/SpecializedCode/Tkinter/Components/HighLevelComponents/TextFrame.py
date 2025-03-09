from ..BasicComponents import Label
from .Base import SimpleHighLevelComponent

class TextFrame(SimpleHighLevelComponent):
    def __init__(self):
        super().__init__()
        self._text = ""
        self._background_color = None
    def _destroy_basic_components(self):
        if self._root_basic_component != None:
            self._root_basic_component.destroy()
            self._root_basic_component = None
    def _simple_create_new_basic_components(self):
        if self.is_able_to_create_new_basic_components():
            self._root_basic_component = Label(self._parent.get_root_basic_component())
    def update(self):
        if self._root_basic_component != None:
            self._root_basic_component.set_text(self._text)
            self._root_basic_component.set_background_color(self._background_color)
            #self._root_basic_component.pack()
            self._root_basic_component.place()
    def set_text(self,text: str):
        self._text = text
        self.update()
    def set_background_color(self,color: str):
        self._background_color = color
        self.update()
    
    
            
