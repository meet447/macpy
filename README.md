# MacPy

MacPy is a Python framework for creating native macOS applications with ease. It provides a Pythonic interface to macOS's native Cocoa framework through PyObjC, making it simple to create authentic macOS applications while maintaining Python's simplicity and elegance.

## Features

- Create native macOS applications using Python
- Access to native macOS UI components (windows, buttons, menus, etc.)
- Simple and intuitive Pythonic API
- Automatic handling of Cocoa event loop
- Easy packaging and distribution of applications

## Installation

```bash
pip install macpy
```

## Quick Start

```python
from macpy import Window, Button

# Create a window
window = Window(title="My App", width=800, height=600)

# Add a button
button = Button(title="Click Me!")
window.add(button)

# Start the application
window.show()
```

## Requirements

- Python 3.7 or higher
- macOS 10.15 or higher
- PyObjC 9.2 or higher

## License

This project is licensed under the MIT License - see the LICENSE file for details.# macpy
