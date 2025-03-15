from ...BaseComponentClasses import UserInterfaceBasicComponent

class BaseAdjustmentStrategy:
        def _tkinter_apply_strategy(self,basic_component: UserInterfaceBasicComponent):
          raise NotImplementedError
        def apply_strategy(self,basic_component: UserInterfaceBasicComponent):
            if not isinstance(basic_component,UserInterfaceBasicComponent):
                raise TypeError
            user_interface_api = basic_component.get_user_interface_api()
            if user_interface_api == "tkinter":
                    self._tkinter_apply_strategy(basic_component)
