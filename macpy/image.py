from Foundation import NSObject, NSMakeRect, NSMakeSize
from AppKit import *
from objc import python_method
from PyObjCTools import AppHelper
import Quartz

class Image:
    def __init__(self, image_path=None, x=0, y=0, width=100, height=100):
        self.native_view = NSImageView.alloc().initWithFrame_(
            NSMakeRect(x, y, width, height)
        )
        if image_path:
            self.set_image(image_path)

    def set_image(self, image_path):
        """Set the image from a file path or URL"""
        if image_path.startswith('http://') or image_path.startswith('https://'):
            import urllib.request, ssl
            from io import BytesIO
            context = ssl._create_unverified_context()
            with urllib.request.urlopen(image_path, context=context) as response:
                image_data = response.read()
            from Foundation import NSData
            image_data = NSData.dataWithBytes_length_(image_data, len(image_data))
            image = NSImage.alloc().initWithData_(image_data)
        else:
            image = NSImage.alloc().initWithContentsOfFile_(image_path)
        self.native_view.setImage_(image)

    def set_position(self, x, y):
        """Set the position of the image"""
        frame = self.native_view.frame()
        new_frame = NSMakeRect(x, y, frame.size.width, frame.size.height)
        self.native_view.setFrame_(new_frame)

    def set_size(self, width, height):
        """Set the size of the image"""
        frame = self.native_view.frame()
        new_frame = NSMakeRect(frame.origin.x, frame.origin.y, width, height)
        self.native_view.setFrame_(new_frame)
        
    def set_corner_radius(self, radius):
        """Set the corner radius of the image"""
        if radius <= 0:
            self.native_view.setWantsLayer_(False)
            return
            
        self.native_view.setWantsLayer_(True)
        self.native_view.layer().setCornerRadius_(radius)
        self.native_view.layer().setMasksToBounds_(True)