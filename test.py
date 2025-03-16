from Prototype import *

print(Adjustment.AdjustmentUnits.BaseAdjustmentUnits)
print(Adjustment.AdjustmentStrategies.BaseAdjustmentStrategy)
print(Adjustment.AdjustmentStrategies.CompositeAdjustmentStrategy)

prop = Adjustment.AdjustmentUnits.ProportionalAdjustmentUnits
abso = Adjustment.AdjustmentUnits.AbsoluteAdjustmentUnits

class strat:
    def apply_strategy(self,basic_component):
        basic_component.place()

adj = Adjustment.AdjustmentStrategies.CompositeAdjustmentStrategy(Adjustment.AdjustmentAnchor.TopLeft,
prop(0.5),prop(0.5),prop(0.0),prop(0.50))
adj2 = Adjustment.AdjustmentStrategies.CompositeAdjustmentStrategy(Adjustment.AdjustmentAnchor.TopLeft,
prop(0.5),prop(0.5),prop(0.5),prop(0.0))
adj3 = Adjustment.AdjustmentStrategies.CompositeAdjustmentStrategy(Adjustment.AdjustmentAnchor.TopLeft,
prop(1.0),abso(15),prop(0.5),prop(0.0))

window = SpecializedCode.Tkinter.Components.HighLevelComponents.TopLevelWindow()
window2 = SpecializedCode.Tkinter.TopLevelInterface.TopLevelWindow()
#window.show()
window2.show()
text = SpecializedCode.Tkinter.Components.HighLevelComponents.TextFrame()
text.set_text("Yellow")
text.set_background_color("Yellow")
text.set_adjustment_strategy(adj)
window.add_child(text)
frame = SpecializedCode.Tkinter.Components.HighLevelComponents.ContainerFrame()
frame.set_background_color("Green")
frame.set_adjustment_strategy(adj2)
window.add_child(frame)
text2 = SpecializedCode.Tkinter.Components.HighLevelComponents.TextFrame()
text2.set_text("Test")
text2.set_background_color("Yellow")
text2.set_adjustment_strategy(adj)
frame.add_child(text2)
frame2 = SpecializedCode.Tkinter.Components.HighLevelComponents.ContainerFrame()
frame2.set_background_color("Blue")
frame2.set_adjustment_strategy(adj2)
frame.add_child(frame2)
text3 = SpecializedCode.Tkinter.Components.HighLevelComponents.TextFrame()
text3.set_text("Test")
text3.set_background_color("Yellow")
text3.set_adjustment_strategy(strat())
frame2.add_child(text3)
frame3 = SpecializedCode.Tkinter.Components.HighLevelComponents.ContainerFrame()
frame3.set_background_color("Red")
frame3.set_adjustment_strategy(adj)
frame2.add_child(frame3)

scrollbar = SpecializedCode.Tkinter.Components.HighLevelComponents.Scroll()
scrollbar.set_adjustment_strategy(adj3)
window.add_child(scrollbar)
