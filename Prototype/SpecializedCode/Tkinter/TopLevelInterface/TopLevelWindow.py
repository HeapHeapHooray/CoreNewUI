import tkinter
from ..TCLRuntimeInitializer import TCLRuntimeInitializer

class TopLevelWindow(TCLRuntimeInitializer):
    def __init__(self):
        super().__init__()
        self._window = tkinter.Toplevel()
        self.hide()
        self._window.pack_propagate(0)
        self._children = []
    def show(self):
        self._window.deiconify()
    def hide(self):
        self._window.withdraw()
    def get_root_basic_component(self):
        return self
    def get_native_basic_component(self):
        return self._window
    def add_child(self,child):
        # This prevents from having duplicate child elements in the list.
        if not child in self._children:
            self._children.append(child)
        # If the child element is already in the list
        # we still update the parent of the child element in case it's not set yet.
        child._set_parent(self)
    def _remove_child_without_updating_child(self,child):
        if not child in self._children:
            return
        self._children.remove(child)
    def remove_child(self,child):
        if not child.get_parent() is self:
            return
        child._set_parent(None)
        _remove_child_without_updating_child(child)
        
        
        
        
