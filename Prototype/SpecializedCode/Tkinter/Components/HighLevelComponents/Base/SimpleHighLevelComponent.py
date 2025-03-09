from ......BaseComponentClasses import UserInterfaceHighLevelComponent

class SimpleHighLevelComponent(UserInterfaceHighLevelComponent):
    def __init__(self):
        self._root_basic_component = None
        self._parent = None
    def get_user_interface_api(self):
        return "tkinter"
    def get_root_basic_component(self):
        return self._root_basic_component
    def get_root_native_basic_component(self):
        if self._root_basic_component is None:
            return None
        return self._root_basic_component.get_native_basic_component()
    def get_parent(self):
        return self._parent
    def _set_parent(self,parent):
        if self._parent != None:
            self._parent._remove_child_without_updating_child(self)
        self._parent = parent
        self._tkinter_new_parent()
    def update(self):
        raise NotImplementedError
    def _simple_create_new_basic_components(self):
        raise NotImplementedError
    def _destroy_basic_components(self):
        raise NotImplementedError
    def _create_new_basic_components(self):
        self._destroy_basic_components()
        self._simple_create_new_basic_components()
    def _tkinter_new_parent(self):
        self._create_new_basic_components_and_update()
    def _create_new_basic_components_and_update(self):
        self._create_new_basic_components()
        self.update()
# Is here to prevent _simple_create_new_basic_components from interacting with
# None objects, even if the high-level component doesn't have an adjustment
# strategy this function should return true if the parent is not None and
# the parent has a root basic component.
    def is_able_to_create_new_basic_components(self):
        instance_has_a_parent = self._parent != None
        if not instance_has_a_parent:
            return False
        parent_has_root_basic_component = self._parent.get_root_basic_component() != None
        if not parent_has_root_basic_component:
            return False
        return True
        
