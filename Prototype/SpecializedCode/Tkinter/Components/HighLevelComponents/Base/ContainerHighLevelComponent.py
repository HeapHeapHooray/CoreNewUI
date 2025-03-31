from .SimpleHighLevelComponent import SimpleHighLevelComponent
from ......Exceptions import CircularHierarchyException

class ContainerHighLevelComponent(SimpleHighLevelComponent):
    def __init__(self):
        super().__init__()
        self._children = []
    def add_child(self,child):
        if child is self:
            return
        current_parent = self
        parents_set = set()
        parents_set.add(child)
        parents_set.add(current_parent)
        while current_parent != None:
            current_parent = current_parent.get_parent()
            if current_parent in parents_set:
                raise CircularHierarchyException
        # This prevents from having duplicate child elements in the list.
        if not child in self._children:
            self._children.append(child)
        # Even if the child element is already in the list
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
    def _create_new_basic_components(self):
        self._destroy_basic_components()
        self._simple_create_new_basic_components()
        # Here we update all the children high-level components after
        # creating the new basic components for the current high-level
        # component (the container).
        for child in self._children:
            child._create_new_basic_components_and_update()
        
