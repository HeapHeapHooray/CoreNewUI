from ..SpecializedCode.Tkinter.Components.HighLevelComponents import TopLevelWindow
from ..SpecializedCode.Tkinter.Components.HighLevelComponents import ImageFrame
from ..Adjustment.AdjustmentStrategies import CompositeAdjustmentStrategy
from ..Adjustment.AdjustmentStrategies import FillAdjustmentStrategy
from ..Adjustment.AdjustmentUnits import ProportionalAdjustmentUnits
from ..Adjustment import AdjustmentAnchor
from PIL import Image,ImageTk

class ImageDisplay:
    def __init__(self):
        self._setup()
    def show(self):
        self._setup()
    def hide(self):
        self.window.close()
    def conf(self,event):
        if event.widget == self.image_frame.get_root_native_basic_component():
            new_image = self.image.copy()
            new_image.thumbnail((event.width,event.height))
            self.image_tk = ImageTk.PhotoImage(new_image)
            self.image_frame.set_image(self.image_tk)
    def _setup(self):
        if hasattr(self,"window"):
            print(self.window.is_open())
            if self.window.is_open():
                return
        prop = ProportionalAdjustmentUnits
        #adj = CompositeAdjustmentStrategy(AdjustmentAnchor.TopLeft,prop(1.0),prop(1.0),prop(0.0),prop(0.0))
        adj = FillAdjustmentStrategy()
        self.image_frame = ImageFrame()
        self.image_frame.set_background_color("Yellow")
        self.image_frame.set_adjustment_strategy(adj)
        self.window = TopLevelWindow()
        self.window.add_child(self.image_frame)
        self.window.set_background_color("Red")
        self.image = Image.open("test.png")
        self.image_frame.get_root_basic_component().bind("<Configure>",self.conf)
