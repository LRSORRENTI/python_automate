# Recap

- PyAutoGUI has a .screenshot method to return an object of the screen, or you can pass in a filepath and name to save it pyautogui.screenshot('./relativePathSS.png')

- locateOnScreen() can be passed a sample file image, and returns the coords of where it found the image

- locateCenterOnScreen() returns an (x, y) tuple of where the image is on screen

- Combining all of these mousemoves, presses, typewriting, and key controls can let you automate many tasks!!
