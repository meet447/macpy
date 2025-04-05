from Foundation import NSObject, NSMakeRect
from AppKit import *
from objc import python_method
from PyObjCTools import AppHelper

class Label:
    def __init__(self, text="Label", x=0, y=0, width=120, height=32):
        self.native_view = NSTextField.alloc().initWithFrame_(
            NSMakeRect(x, y, width, height)
        )
        self.native_view.setStringValue_(text)
        self.native_view.setBezeled_(False)
        self.native_view.setEditable_(False)
        self.native_view.setSelectable_(False)
        self.native_view.setBackgroundColor_(NSColor.clearColor())

    def set_text(self, text):
        """Set the text of the label"""
        self.native_view.setStringValue_(text)

    def set_position(self, x, y):
        """Set the position of the label"""
        frame = self.native_view.frame()
        new_frame = NSMakeRect(x, y, frame.size.width, frame.size.height)
        self.native_view.setFrame_(new_frame)

    def set_size(self, width, height):
        """Set the size of the label"""
        frame = self.native_view.frame()
        new_frame = NSMakeRect(frame.origin.x, frame.origin.y, width, height)
        self.native_view.setFrame_(new_frame)