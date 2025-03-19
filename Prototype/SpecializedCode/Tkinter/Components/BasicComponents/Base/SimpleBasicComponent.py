from .... import TCLRuntimeInitializer
from ......BaseComponentClasses import UserInterfaceBasicComponent
from ..Common import get_tcl_error_handling_context,handle_tcl_error

class SimpleBasicComponent(TCLRuntimeInitializer,UserInterfaceBasicComponent):
    def __init__(self,parent,native_basic_component_type):
        TCLRuntimeInitializer.__init__(self)
        UserInterfaceBasicComponent.__init__(self)
        self._native_basic_component = None
        self._parent = parent
        self._create_native_basic_component(native_basic_component_type)
        
    # SHOULD NOT handle tcl errors since we want the exception to raise when, for some reason, the component
    # can't be created, there is a problem with it though, since we can create a native basic component
    # for a parent native basic component that has been deleted by another thread (asynchronously).
    def _create_native_basic_component(self,native_basic_component_type):
        parent_native_basic_component = None
        if self._parent != None:
            parent_native_basic_component = self._parent.get_native_basic_component()
        self._native_basic_component = native_basic_component_type(parent_native_basic_component)
    def get_user_interface_api(self) -> str:
        return "tkinter"
    def get_native_basic_component(self):
        return self._native_basic_component
    def get_parent(self):
        return self._parent
    # Does not need to handle tcl errors
    def destroy(self):
        self._native_basic_component.destroy()
    # Does not need to handle tcl errors
    def is_valid(self):
        exists: int = self._native_basic_component.winfo_exists()

        if exists == 1:
            return True

        return False
    def get_native_basic_component_system_handle_or_default(self,default=None):
        output = default
        with get_tcl_error_handling_context() as _:
            output = self._native_basic_component.winfo_id()
        return output
    @handle_tcl_error
    def place(self,**args):
        self._native_basic_component.place(**args)
    @handle_tcl_error
    def bind(self,*args):
        self._native_basic_component.bind(*args)
