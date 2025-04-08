from macpy import Window, Image, Label, Sidebar

# Create main window with dark theme
window = Window('Mac App Store', width=1200, height=800)
window.set_background_color('#1C1C1E')

# Create and configure sidebar
sidebar = Sidebar.sidebarWithFrame_(x=0, y=0, width=280, height=800)

# Add navigation items with SF Symbols icons
sidebar.add_item('Discover')
sidebar.add_item('Arcade')
sidebar.add_item('Create')
sidebar.add_item('Work')
sidebar.add_item('Play')
sidebar.add_item('Develop')
sidebar.add_item('Categories')

window.add(sidebar)

# Header section with SF Pro Display font
header_label = Label('GAMES WE LOVE', x=320, y=740, width=200, height=30)
header_label.set_text_color('#FFFFFF')
header_label.set_font_size(13)
header_label.set_font_weight('semibold')
window.add(header_label)

# Featured game section with improved typography
title_label = Label("Assassin's Creed Shadows Is Here!", x=320, y=690, width=600, height=40)
title_label.set_text_color('#FFFFFF')
title_label.set_font_size(32)
title_label.set_font_weight('bold')
window.add(title_label)

desc_label = Label('The epic action saga heads to Japan.', x=320, y=660, width=400, height=30)
desc_label.set_text_color('#999999')
desc_label.set_font_size(17)
desc_label.set_font_weight('regular')
window.add(desc_label)

# Featured game image with rounded corners
featured_image = Image('https://cdn.wccftech.com/wp-content/uploads/2024/09/Assassins-Creed-Shadows.jpg',
                      x=320, y=360, width=840, height=280)
featured_image.set_corner_radius(12)
window.add(featured_image)

# App cards section with improved spacing
apps_header = Label('Apps and Games We Love Right Now', x=320, y=300, width=400, height=30)
apps_header.set_text_color('#FFFFFF')
apps_header.set_font_size(22)
apps_header.set_font_weight('semibold')
window.add(apps_header)

# App card 1 with rounded corners and shadow
app1_image = Image('https://images.unsplash.com/photo-1614680376573-df3480f0c6ff?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1974&q=80',
                   x=320, y=160, width=140, height=140)
app1_image.set_corner_radius(20)
window.add(app1_image)

app1_title = Label('Control Ultimate Edition', x=320, y=120, width=140, height=20)
app1_title.set_text_color('#FFFFFF')
app1_title.set_font_size(14)
app1_title.set_font_weight('medium')
window.add(app1_title)

# App card 2 with rounded corners and shadow
app2_image = Image('https://images.unsplash.com/photo-1618172193763-c511deb635ca?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=2064&q=80',
                   x=480, y=160, width=140, height=140)
app2_image.set_corner_radius(20)
window.add(app2_image)

app2_title = Label('Final Cut Pro', x=480, y=120, width=140, height=20)
app2_title.set_text_color('#FFFFFF')
app2_title.set_font_size(14)
app2_title.set_font_weight('medium')
window.add(app2_title)

# Show the window
window.show()