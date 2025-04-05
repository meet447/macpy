from macpy import Window, Label, Button, TextInput, Checkbox, Image, Slider

class DemoApp:
    def __init__(self):
        self.window = Window('Demo App', width=800, height=600)
        self.create_ui()

    def create_ui(self):
        # Label
        self.label = Label('Welcome to MacPy Demo', x=20, y=500)
        self.window.add(self.label)

        # Button
        self.button = Button('Click Me', x=20, y=450, width=100, height=30)
        self.button.set_callback(self.on_button_click)
        self.window.add(self.button)

        # TextInput
        self.text_input = TextInput(placeholder='Enter text here', x=20, y=400)
        self.text_input.set_callback(self.on_text_change)
        self.window.add(self.text_input)

        # Checkbox
        self.checkbox = Checkbox('Enable Feature', x=20, y=350)
        self.checkbox.set_callback(self.on_checkbox_toggle)
        self.window.add(self.checkbox)

        # Image
        self.image = Image('https://assets-prd.ignimgs.com/2023/10/26/shonen-jump-1698339063704.jpg', x=20, y=200, width=200, height=200)
        self.window.add(self.image)

        # Slider
        self.slider = Slider(x=20, y=150, width=200)
        self.slider.set_callback(self.on_slider_change)
        self.window.add(self.slider)

    def on_button_click(self):
        self.label.set_text('Button was clicked!')

    def on_text_change(self, text):
        self.label.set_text(f'You typed: {text}')

    def on_checkbox_toggle(self, state):
        self.label.set_text(f'Checkbox is {"enabled" if state else "disabled"}')

    def on_slider_change(self, value):
        self.label.set_text(f'Slider value: {value}')

if __name__ == '__main__':
    app = DemoApp()
    app.window.show()