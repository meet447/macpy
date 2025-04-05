from macpy import Image, Window

window = Window('Image Example', width=400, height=300)

image = Image('https://images.unsplash.com/photo-1575936123452-b67c3203c357?fm=jpg&q=60&w=3000&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8aW1hZ2V8ZW58MHx8MHx8fDA%3D', x=50, y=50, width=200, height=200)

window.add(image)
window.show()