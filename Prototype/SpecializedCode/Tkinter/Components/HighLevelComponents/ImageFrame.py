from ..BasicComponents import Label
from .Base import SimpleHighLevelComponent
from PIL import ImageTk

class ImageFrame(SimpleHighLevelComponent):
    def __init__(self):
        super().__init__()
        self._image = None
        self._background_color = None
    def _destroy_basic_components(self):
        if self._root_basic_component != None:
            self._root_basic_component.destroy()
            self._root_basic_component = None
    def _simple_create_new_basic_components(self):
        if self.is_able_to_create_new_basic_components():
            self._root_basic_component = Label(self._parent.get_root_basic_component())
    def update(self):
        if self._root_basic_component != None and self._adjustment_strategy != None:
            self._root_basic_component.set_image(self._image)
            self._root_basic_component.set_background_color(self._background_color)
            self._adjustment_strategy.apply_strategy(self._root_basic_component)
    def set_image(self,image: ImageTk):
        self._image = image
        self.update()
    def set_background_color(self,color: str):
        self._background_color = color
        self.update()
    
    
             
