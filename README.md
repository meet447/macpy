# MacPy - macOS GUI Framework

MacPy is a Python framework for creating native macOS GUI applications using PyObjC.

## Features

- Native macOS UI components
- Simple and intuitive API
- Callback support for user interactions
- URL image loading functionality

## Installation

```bash
pip install macpy
```

## Usage

### Window

```python
from macpy.window import Window

window = Window('My Window', 800, 600)
window.show()
```

### Button

```python
from macpy.button import Button

def on_click(): print('Button clicked!')

button = Button('Click Me', on_click)
window.add(button)
```

### Label

```python
from macpy.label import Label

label = Label('Hello, World!')
window.add(label)
```

### Image

```python
from macpy.image import Image

# Load from local file
image = Image('local_image.png')

# Load from URL
image = Image('https://example.com/remote_image.png')

window.add(image)
```

### Slider

```python
from macpy.slider import Slider

def on_value_change(value): print(f'New value: {value}')

slider = Slider()
slider.set_callback(on_value_change)
window.add(slider)
```

### Dropdown

```python
from macpy.dropdown import Dropdown

def on_select(index): print(f'Selected index: {index}')

dropdown = Dropdown(['Option 1', 'Option 2', 'Option 3'])
dropdown.set_callback(on_select)
window.add(dropdown)
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)
