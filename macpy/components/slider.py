from Foundation import NSObject, NSMakeRect
from AppKit import *
from objc import python_method
from PyObjCTools import AppHelper

class Slider:
    def __init__(self, min_value=0, max_value=100, x=0, y=0, width=200, height=32):
        self.native_view = NSSlider.alloc().initWithFrame_(
            NSMakeRect(x, y, width, height)
        )
        self.native_view.setMinValue_(min_value)
        self.native_view.setMaxValue_(max_value)
        self.native_view.setTarget_(self)
        self.native_view.setAction_(b'value_changed:')

        # Store the callback function
        self._callback = None

    def set_callback(self, callback):
        """Set the callback function to be called when the value changes"""
        self._callback = callback

    @python_method
    def value_changed_(self, sender):
        """Internal method to handle value changes"""
        if self._callback:
            self._callback(self.native_view.floatValue())

    def set_position(self, x, y):
        """Set the position of the slider"""
        frame = self.native_view.frame()
        new_frame = NSMakeRect(x, y, frame.size.width, frame.size.height)
        self.native_view.setFrame_(new_frame)

    def set_size(self, width, height):
        """Set the size of the slider"""
        frame = self.native_view.frame()
        new_frame = NSMakeRect(frame.origin.x, frame.origin.y, width, height)
        self.native_view.setFrame_(new_frame)