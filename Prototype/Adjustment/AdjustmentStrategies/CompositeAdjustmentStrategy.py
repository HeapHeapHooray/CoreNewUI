from typing import Union
from .BaseAdjustmentStrategy import BaseAdjustmentStrategy
from ..AdjustmentAnchor import AdjustmentAnchor
from ..AdjustmentUnits import AbsoluteAdjustmentUnits,ProportionalAdjustmentUnits
from ...BaseComponentClasses import UserInterfaceBasicComponent

class CompositeAdjustmentStrategy(BaseAdjustmentStrategy):
    def __init__(self,adjustment_anchor: AdjustmentAnchor,height: Union[AbsoluteAdjustmentUnits,ProportionalAdjustmentUnits],width: Union[AbsoluteAdjustmentUnits,ProportionalAdjustmentUnits],
                        x_position: Union[AbsoluteAdjustmentUnits,ProportionalAdjustmentUnits],y_position: Union[AbsoluteAdjustmentUnits,ProportionalAdjustmentUnits]):
        self.adjustment_anchor = adjustment_anchor
        self.height = height
        self.width = width
        self.x_position = x_position
        self.y_position = y_position

    def _tkinter_apply_strategy(self,basic_component: UserInterfaceBasicComponent):
        args = {}
        
        if isinstance(self.height,ProportionalAdjustmentUnits):
            args["relheight"] = self.height.value_in_units
        else:
            args["height"] = self.height.value_in_units
            
        if isinstance(self.width,ProportionalAdjustmentUnits):
            args["relwidth"] = self.width.value_in_units
        else:
            args["width"] = self.width.value_in_units
            
        if isinstance(self.x_position,ProportionalAdjustmentUnits):
            args["relx"] = self.x_position.value_in_units
        else:
            args["x"] = self.x_position.value_in_units
            
        if isinstance(self.y_position,ProportionalAdjustmentUnits):
            args["rely"] = self.y_position.value_in_units
        else:
            args["y"] = self.y_position.value_in_units

        args["anchor"] = self.adjustment_anchor.value

        basic_component.place(**args)
