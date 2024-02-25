# Controlling the mouse 

import pyautogui

print(pyautogui.size())
# Size(width=1920, height=1080)
# This returns the size of the display

print(pyautogui.position())
# This returns the x and y coordinates of 
# where the mouse is positioned on the screen:
# Point(x=984, y=816)

# This first function we'll use to control the mouse 
# is, we pass the moveTo function (x-cord, y-cord):

# pyautogui.moveTo(10, 10)

# You can also mimic what a human-scroll looks 
# like be passing in a duration to the mvoeTo

# pyautogui.moveTo(50, 50, duration=5)

# Also can move the mouse cursor relative to where 
# it currently is:

# pyautogui.moveRel(200, 0)
# The above instantly moves the cursor 200px to the right 
# pyautogui.moveRel(0, -300, duration=4)
# Pass in negative y coords to go upwards, and negative 
# x coords to go left along the x-axis

# NOTE A very easy way to check where to postion the mouse 
# to click is to first put it where the desired 
# button or action is and call the .position 
# method:

print(pyautogui.position())

# Now to click when at the desired postiion:
pyautogui.moveTo(x=822,y=30, duration=5)
pyautogui.click(x=822,y=30)

# There are other useful methods, like double click 
# for certain elements on a page that require it, 
# like opening a desktop shortcut icon

# There is also:
# pyautogui.dragRel()
# which will simulated pressing the left mouse button
# and dragging