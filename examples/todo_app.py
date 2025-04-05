from macpy import Window, Button, TextInput, Checkbox
from AppKit import NSMakeRect

class TodoApp:
    def __init__(self):
        self.window = Window('Todo App', width=400, height=600)
        self.tasks = []

        # Create UI components
        self.input = TextInput(placeholder='Enter new task', x=20, y=540, width=280)
        self.add_button = Button('Add', x=310, y=540, width=70)

        # Set up event handlers
        self.add_button.set_callback(self.add_task)

        # Add components to window
        self.window.add(self.input)
        self.window.add(self.add_button)

    def add_task(self):
        task_text = self.input.native_view.stringValue()
        if task_text:
            y = 500 - len(self.tasks) * 40
            task = Checkbox(task_text, x=20, y=y, width=360)
            self.tasks.append(task)
            self.window.add(task)
            self.input.native_view.setStringValue_('')

    def run(self):
        self.window.show()

if __name__ == '__main__':
    app = TodoApp()
    app.run()