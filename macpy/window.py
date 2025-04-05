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
        self.window.setBackgroundColor_(NSColor.windowBackgroundColor())
        self.window.center()
    
        # Create a content view for adding subviews
        self.content_view = self.window.contentView()
    
    def add(self, component):
        """Add a UI component to the window"""
        if hasattr(component, 'native_view'):
            self.content_view.addSubview_(component.native_view)
    
    def show(self):
        """Show the window and start the application"""
        self.window.makeKeyAndOrderFront_(None)
        AppHelper.runEventLoop()