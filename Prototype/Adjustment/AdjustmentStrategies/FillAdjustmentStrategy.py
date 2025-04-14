from .BaseAdjustmentStrategy import BaseAdjustmentStrategy
from .CompositeAdjustmentStrategy import CompositeAdjustmentStrategy
from ..AdjustmentAnchor import AdjustmentAnchor
from ..AdjustmentUnits import ProportionalAdjustmentUnits
from ...BaseComponentClasses import UserInterfaceBasicComponent

class FillAdjustmentStrategy(BaseAdjustmentStrategy):
    def __init__(self):
        pass
    def _apply_strategy_user_interface_api_agnostic(self,basic_component: UserInterfaceBasicComponent):
        strategy = CompositeAdjustmentStrategy(AdjustmentAnchor.TopLeft,ProportionalAdjustmentUnits(1.0),ProportionalAdjustmentUnits(1.0),ProportionalAdjustmentUnits(0.0),ProportionalAdjustmentUnits(0.0))
        strategy.apply_strategy(basic_component)
    _tkinter_apply_strategy = _apply_strategy_user_interface_api_agnostic
