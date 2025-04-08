from Foundation import *
from AppKit import *
from PyObjCTools import AppHelper

class Window:
    def __init__(self, title="Untitled", width=800, height=600, resizable=True):
        self.width = width
        self.height = height
        self.resizable = resizable
    
        # Create the application instance
        if not NSApp():
            NSApplication.sharedApplication()
            NSApp().setActivationPolicy_(NSApplicationActivationPolicyRegular)
    
        # Create the window
        style_mask = NSWindowStyleMaskTitled | NSWindowStyleMaskClosable | NSWindowStyleMaskMiniaturizable
        if resizable:
            style_mask |= NSWindowStyleMaskResizable
    
        self.window = NSWindow.alloc().initWithContentRect_styleMask_backing_defer_(
            NSMakeRect(0, 0, width, height),
            style_mask,
            NSBackingStoreBuffered,
            False
        )
    
        self.window.setTitle_(title)
        self.window.center()
        
        # Initialize content view first
        self.content_view = self.window.contentView()
        
        # Set window background color
        self.window.setBackgroundColor_(NSColor.windowBackgroundColor())
        self.set_background_color('#1C1C1E')

    def set_background_color(self, color_hex):
        """Set the background color of the window using hex color code"""
        # Convert hex to RGB
        color_hex = color_hex.lstrip('#')
        rgb = tuple(int(color_hex[i:i+2], 16)/255.0 for i in (0, 2, 4))
        
        # Create NSColor from RGB values
        ns_color = NSColor.colorWithRed_green_blue_alpha_(*rgb, 1.0)
        self.window.setBackgroundColor_(ns_color)
    
    def add(self, component):
        """Add a UI component to the window"""
        if hasattr(component, 'native_view'):
            self.content_view.addSubview_(component.native_view)
    
    def show(self):
        """Show the window and start the application"""
        self.window.makeKeyAndOrderFront_(None)
        AppHelper.runEventLoop()