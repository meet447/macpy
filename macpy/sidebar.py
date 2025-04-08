from Foundation import NSObject, NSMakeRect
from AppKit import *
import objc
from objc import python_method
from PyObjCTools import AppHelper

class SidebarItem:
    def __init__(self, title, icon_path=None):
        self.title = title
        self.icon_path = icon_path

class Sidebar(NSObject):
    def init(self):
        self = objc.super(Sidebar, self).init()
        if self is None: return None
        return self

    def initWithFrame_(self, frame):
        self = objc.super(Sidebar, self).init()
        if self is None: return None
        
        # Create and configure scroll view
        self.native_view = NSScrollView.alloc().initWithFrame_(frame)
        self.native_view.setHasVerticalScroller_(True)
        self.native_view.setAutohidesScrollers_(True)
        self.native_view.setBorderType_(NSNoBorder)
        self.native_view.setBackgroundColor_(NSColor.colorWithRed_green_blue_alpha_(0.145, 0.145, 0.161, 1.0))
        
        # Create table view
        self.table_view = NSTableView.alloc().initWithFrame_(NSMakeRect(0, 0, frame.size.width, frame.size.height))
        self.table_view.setBackgroundColor_(NSColor.clearColor())
        self.table_view.setHeaderView_(None)
        self.table_view.setSelectionHighlightStyle_(NSTableViewSelectionHighlightStyleSourceList)
        
        # Add column for content
        column = NSTableColumn.alloc().initWithIdentifier_('content')
        column.setWidth_(frame.size.width)
        self.table_view.addTableColumn_(column)
        
        # Set up data source
        self.items = []
        self.table_view.setDataSource_(self)
        self.table_view.setDelegate_(self)
        
        # Set table view as document view
        self.native_view.setDocumentView_(self.table_view)
        
        return self
    
    @classmethod
    def sidebarWithFrame_(cls, x=0, y=0, width=280, height=800):
        instance = cls.alloc().initWithFrame_(NSMakeRect(x, y, width, height))
        return instance
    
    def add_item(self, title, icon_path=None):
        """Add an item to the sidebar"""
        item = SidebarItem(title, icon_path)
        self.items.append(item)
        self.table_view.reloadData()
    
    def numberOfRowsInTableView_(self, table_view):
        return len(self.items)
    
    def tableView_objectValueForTableColumn_row_(self, table_view, column, row):
        return self.items[row].title
    
    @python_method
    def tableView_viewForTableColumn_row_(self, table_view, column, row):
        item = self.items[row]
        
        # Create cell view
        cell_view = NSTableCellView.alloc().init()
        
        # Create and configure text field
        text_field = NSTextField.alloc().initWithFrame_(NSMakeRect(0, 0, column.width(), 20))
        text_field.setStringValue_(item.title)
        text_field.setBezeled_(False)
        text_field.setDrawsBackground_(False)
        text_field.setEditable_(False)
        text_field.setSelectable_(False)
        text_field.setTextColor_(NSColor.whiteColor())
        
        # Add icon if provided
        if item.icon_path:
            image_view = NSImageView.alloc().initWithFrame_(NSMakeRect(0, 0, 16, 16))
            image = NSImage.alloc().initWithContentsOfFile_(item.icon_path)
            image_view.setImage_(image)
            cell_view.setImageView_(image_view)
            text_field.setFrame_(NSMakeRect(24, 0, column.width() - 24, 20))
        
        cell_view.setTextField_(text_field)
        return cell_view
    
    def set_position(self, x, y):
        """Set the position of the sidebar"""
        frame = self.native_view.frame()
        new_frame = NSMakeRect(x, y, frame.size.width, frame.size.height)
        self.native_view.setFrame_(new_frame)
    
    def set_size(self, width, height):
        """Set the size of the sidebar"""
        frame = self.native_view.frame()
        new_frame = NSMakeRect(frame.origin.x, frame.origin.y, width, height)
        self.native_view.setFrame_(new_frame)