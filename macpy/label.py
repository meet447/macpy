from Foundation import NSObject, NSMakeRect
from AppKit import *
from objc import python_method
from PyObjCTools import AppHelper

# Font weight constants
FONT_WEIGHTS = {
    'regular': 5,
    'medium': 6,
    'semibold': 8,
    'bold': 9
}

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

    def set_text_color(self, color_hex):
        """Set the text color using hex color code"""
        color_hex = color_hex.lstrip('#')
        rgb = tuple(int(color_hex[i:i+2], 16)/255.0 for i in (0, 2, 4))
        ns_color = NSColor.colorWithRed_green_blue_alpha_(*rgb, 1.0)
        self.native_view.setTextColor_(ns_color)

    def set_font_size(self, size):
        """Set the font size"""
        font = NSFont.systemFontOfSize_(size)
        self.native_view.setFont_(font)
        
    def set_font_weight(self, weight):
        """Set the font weight (regular, medium, semibold, bold)"""
        if weight not in FONT_WEIGHTS:
            raise ValueError(f"Invalid font weight. Must be one of: {', '.join(FONT_WEIGHTS.keys())}")
            
        current_font = self.native_view.font()
        font_manager = NSFontManager.sharedFontManager()
        weighted_font = font_manager.fontWithFamily_traits_weight_size_(
            current_font.familyName(),
            0,  # No special traits
            FONT_WEIGHTS[weight],
            current_font.pointSize()
        )
        self.native_view.setFont_(weighted_font)