from macpy import Window, Button

def button_clicked():
    print("Button clicked!")

# Create the main window
window = Window(title="MacPy Demo", width=400, height=300)

# Create a button and set its position
button = Button(title="Click Me!")
button.set_position(140, 130)  # Center the button in the window
button.set_callback(button_clicked)

# Add the button to the window
window.add(button)

# Show the window and start the application
window.show()