from .Base import ContainerHighLevelComponent
from ..BasicComponents import Toplevel

class TopLevelWindow(ContainerHighLevelComponent):
    def __init__(self):
        super().__init__()
        self._root_basic_component = Toplevel()
        self._root_basic_component.set_pack_propagation(should_propagate=False)
    def set_background_color(self,color: str):
        self._root_basic_component.set_background_color(color)
