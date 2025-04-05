from Foundation import NSObject, NSMakeRect
from AppKit import *
from objc import python_method
from PyObjCTools import AppHelper

class ProgressBar:
    def __init__(self, x=0, y=0, width=200, height=20):
        self.native_view = NSProgressIndicator.alloc().initWithFrame_(
            NSMakeRect(x, y, width, height)
        )
        self.native_view.setStyle_(NSProgressIndicatorStyleBar)
        self.native_view.setIndeterminate_(False)
        self.native_view.setMinValue_(0)
        self.native_view.setMaxValue_(100)
        self.native_view.setDoubleValue_(0)
    
    def set_progress(self, value):
        """Set the progress value (0-100)"""
        self.native_view.setDoubleValue_(value)
    
    def set_position(self, x, y):
        """Set the position of the progress bar"""
        frame = self.native_view.frame()
        new_frame = NSMakeRect(x, y, frame.size.width, frame.size.height)
        self.native_view.setFrame_(new_frame)
    
    def set_size(self, width, height):
        """Set the size of the progress bar"""
        frame = self.native_view.frame()
        new_frame = NSMakeRect(frame.origin.x, frame.origin.y, width, height)
        self.native_view.setFrame_(new_frame)