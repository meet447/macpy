from Foundation import NSObject, NSMakeRect
from AppKit import *
from objc import python_method
from PyObjCTools import AppHelper

class TextInput:
    def __init__(self, placeholder="", x=0, y=0, width=200, height=32):
        self.native_view = NSTextField.alloc().initWithFrame_(
            NSMakeRect(x, y, width, height)
        )
        self.native_view.setPlaceholderString_(placeholder)
        self.native_view.setBezelStyle_(NSTextFieldSquareBezel)
        self.native_view.setTarget_(self)
        self.native_view.setAction_(b'text_changed:')

        # Store the callback function
        self._callback = None

    def set_callback(self, callback):
        """Set the callback function to be called when the text changes"""
        self._callback = callback

    @python_method
    def text_changed_(self, sender):
        """Internal method to handle text changes"""
        if self._callback:
            self._callback(self.native_view.stringValue())

    def set_position(self, x, y):
        """Set the position of the text input"""
        frame = self.native_view.frame()
        new_frame = NSMakeRect(x, y, frame.size.width, frame.size.height)
        self.native_view.setFrame_(new_frame)

    def set_size(self, width, height):
        """Set the size of the text input"""
        frame = self.native_view.frame()
        new_frame = NSMakeRect(frame.origin.x, frame.origin.y, width, height)
        self.native_view.setFrame_(new_frame)