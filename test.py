from Prototype import *

class strat:
    def apply_strategy(self,basic_component):
        basic_component.place()

window = SpecializedCode.Tkinter.Components.HighLevelComponents.TopLevelWindow()
window2 = SpecializedCode.Tkinter.TopLevelInterface.TopLevelWindow()
#window.show()
window2.show()
text = SpecializedCode.Tkinter.Components.HighLevelComponents.TextFrame()
text.set_text("Test")
text.set_background_color("Yellow")
text.set_adjustment_strategy(strat())
window.add_child(text)
frame = SpecializedCode.Tkinter.Components.HighLevelComponents.ContainerFrame()
frame.set_background_color("Green")
window.add_child(frame)
text2 = SpecializedCode.Tkinter.Components.HighLevelComponents.TextFrame()
text2.set_text("Test")
text2.set_background_color("Yellow")
text2.set_adjustment_strategy(strat())
frame.add_child(text2)
frame2 = SpecializedCode.Tkinter.Components.HighLevelComponents.ContainerFrame()
frame2.set_background_color("Blue")
frame.add_child(frame2)
text3 = SpecializedCode.Tkinter.Components.HighLevelComponents.TextFrame()
text3.set_text("Test")
text3.set_background_color("Yellow")
text3.set_adjustment_strategy(strat())
frame2.add_child(text3)
frame3 = SpecializedCode.Tkinter.Components.HighLevelComponents.ContainerFrame()
frame3.set_background_color("Red")
frame2.add_child(frame3)
