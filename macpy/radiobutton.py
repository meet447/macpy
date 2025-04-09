from Foundation import NSObject, NSMakeRect
from AppKit import *
from objc import python_method
from PyObjCTools import AppHelper

class RadioButton:
    def __init__(self, title="Radio Button", x=0, y=0, width=120, height=32):
        self.native_view = NSButton.alloc().initWithFrame_(
            NSMakeRect(x, y, width, height)
        )
        self.native_view.setTitle_(title)
        self.native_view.setButtonType_(NSButtonTypeRadio)
        self.native_view.setTarget_(self)
        self.native_view.setAction_(b'button_clicked:')
        
        # Store the callback function
        self._callback = None
    
    def set_callback(self, callback):
        """Set the callback function to be called when the radio button is clicked"""
        self._callback = callback
    
    @python_method
    def button_clicked_(self, sender):
        """Internal method to handle radio button clicks"""
        if self._callback:
            self._callback()
    
    def set_position(self, x, y):
        """Set the position of the radio button"""
        frame = self.native_view.frame()
        new_frame = NSMakeRect(x, y, frame.size.width, frame.size.height)
        self.native_view.setFrame_(new_frame)
    
    def set_size(self, width, height):
        """Set the size of the radio button"""
        frame = self.native_view.frame()
        new_frame = NSMakeRect(frame.origin.x, frame.origin.y, width, height)
        self.native_view.setFrame_(new_frame)