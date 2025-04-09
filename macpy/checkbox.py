from Foundation import NSObject, NSMakeRect
from AppKit import *
from objc import python_method
from PyObjCTools import AppHelper

class Checkbox:
    def __init__(self, label="", x=0, y=0, width=120, height=32):
        self.native_view = NSButton.alloc().initWithFrame_(
            NSMakeRect(x, y, width, height)
        )
        self.native_view.setButtonType_(NSSwitchButton)
        self.native_view.setTitle_(label)
        self.native_view.setTarget_(self)
        self.native_view.setAction_(b'state_changed:')

        # Store the callback function
        self._callback = None

    def set_callback(self, callback):
        """Set the callback function to be called when the state changes"""
        self._callback = callback

    @python_method
    def state_changed_(self, sender):
        """Internal method to handle state changes"""
        if self._callback:
            self._callback(self.native_view.state())

    def set_position(self, x, y):
        """Set the position of the checkbox"""
        frame = self.native_view.frame()
        new_frame = NSMakeRect(x, y, frame.size.width, frame.size.height)
        self.native_view.setFrame_(new_frame)

    def set_size(self, width, height):
        """Set the size of the checkbox"""
        frame = self.native_view.frame()
        new_frame = NSMakeRect(frame.origin.x, frame.origin.y, width, height)
        self.native_view.setFrame_(new_frame)