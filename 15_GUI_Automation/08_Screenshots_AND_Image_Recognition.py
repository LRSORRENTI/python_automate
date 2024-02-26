# Screenshots and image recognition

# PyAutoGUI has a feature to take a screenshot, 
# on LINUX you'll need to run:
# sudo apt-get install scrot  

# Windows or Mac, only pyautogui is required

import pyautogui

pyautogui.screenshot()

# the above returns an image object, pillow is 
# an image module that's used to supplement 
# pyautoguis screenshot method

# we pass in a file location of a screenshot: 
pyautogui.press('f11')
# pyautogui.screenshot('C:\\Users\\specify absolute path to save scrrenshot elsewhere')
pyautogui.screenshot('./relativePathSS2.png')