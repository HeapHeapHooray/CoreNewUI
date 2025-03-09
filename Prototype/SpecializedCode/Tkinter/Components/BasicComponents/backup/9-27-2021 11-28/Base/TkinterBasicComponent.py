from .... import TCLRuntimeInitializer

class TkinterBasicComponent(TCLRuntimeInitializer):
    def __init__(self):
        super().__init__()
        self._native_basic_component = None
        self._parent = None
    def get_root_native_basic_component(self):
        return self._native_basic_component
    def get_parent(self):
        return self._parent
    def set_parent(self,parent):
        self._parent = parent
        self.update()
    def update(self):
        self._recreate_basic_component()
    def _create_basic_component(self):
        raise NotImplementedError
    def _destroy_basic_component(self):
        raise NotImplementedError
    def _recreate_basic_component(self):
        self._destroy_basic_component()
        self._create_basic_component()
