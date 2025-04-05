# MacPy - Python GUI Framework for macOS

MacPy is a Python framework for creating native macOS applications using PyObjC. It provides simple and intuitive components for building user interfaces.

## Features

- Native macOS UI components
- Simple API for creating windows and controls
- Support for common UI elements:
  - Window
  - Button
  - Label
  - Image
  - Checkbox
  - Slider
  - TextInput
- Callback support for interactive components
- URL image loading functionality

## Installation

```bash
pip install macpy
```

## Usage

### Basic Window

```python
from macpy import Window

window = Window('My Window', width=800, height=600)
window.show()
```

### Button with Callback

```python
from macpy import Button, Window

window = Window('Button Example', width=400, height=300)

button = Button('Click Me', x=50, y=50, width=100, height=32)
button.set_callback(lambda: print('Button clicked!'))

window.add(button)
window.show()
```

### Label

```python
from macpy import Label, Window

window = Window('Label Example', width=400, height=300)

label = Label('Hello, MacPy!', x=50, y=50, width=200, height=32)

window.add(label)
window.show()
```

### Image from URL

```python
from macpy import Image, Window

window = Window('Image Example', width=400, height=300)

image = Image('https://example.com/image.png', x=50, y=50, width=200, height=200)

window.add(image)
window.show()
```

## Components Documentation

### Window

- `Window(title, width, height)`
- `show()` - Display the window
- `add(component)` - Add a UI component to the window

### Button

- `Button(text, x, y, width, height)`
- `set_callback(callback)` - Set click handler

### Label

- `Label(text, x, y, width, height)`
- `set_text(text)` - Update label text

### Image

- `Image(image_path, x, y, width, height)`
  - Supports both local files and URLs
- `set_image(image_path)` - Change the image

For more examples, see the `examples/` directory.

## License

MIT
