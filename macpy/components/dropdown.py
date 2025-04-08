from Foundation import NSObject, NSMakeRect
from AppKit import *
from objc import python_method
from PyObjCTools import AppHelper

class Dropdown:
    def __init__(self, items=[], x=0, y=0, width=120, height=32):
        self.native_view = NSPopUpButton.alloc().initWithFrame_(
            NSMakeRect(x, y, width, height)
        )
        self.set_items(items)
        self.native_view.setTarget_(self)
        self.native_view.setAction_(b'selection_changed:')
        
        # Store the callback function
        self._callback = None
    
    def set_callback(self, callback):
        """Set the callback function to be called when the dropdown selection changes"""
        self._callback = callback
    
    def set_items(self, items):
        """Set the items in the dropdown"""
        self.native_view.removeAllItems()
        self.native_view.addItemsWithTitles_(items)
    
    @python_method
    def selection_changed_(self, sender):
        """Internal method to handle dropdown selection changes"""
        if self._callback:
            selected_index = self.native_view.indexOfSelectedItem()
            self._callback(selected_index)
    
    def set_position(self, x, y):
        """Set the position of the dropdown"""
        frame = self.native_view.frame()
        new_frame = NSMakeRect(x, y, frame.size.width, frame.size.height)
        self.native_view.setFrame_(new_frame)
    
    def set_size(self, width, height):
        """Set the size of the dropdown"""
        frame = self.native_view.frame()
        new_frame = NSMakeRect(frame.origin.x, frame.origin.y, width, height)
        self.native_view.setFrame_(new_frame)