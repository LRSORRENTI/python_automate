# Recap

- Controlling the mouse and keyboard is called GUI automation

- The PyAutoGUI third party module has many functions to control the mouse and keyboard

- pyautogui.size() returns the size of the monitor and screen resolution

- pyautogui.position() returns the mouse position in x and y coords

- To find the x and y coords much faster use print(pyautogui.displayMousePosition()) which will dynamically show in the terminal what the mouse x and y positions are

- pyautogui.moveTo() moves the mouse to the given coord

- The mouse move is instant, to simulate a actual mouse move, pass in a value to duration

- pyautogui.moveRel() will move the mouse relative to it's current position

- pyautogui.click, pyautogui.doubleClick, pyautogui.rightClick, and pyautogui.middleClick are all available mouse functions

- dragTo() and relTo() can be used to simulate clicking and dragging

- If a program gets out of your control, slam the mouse as hard as possible to the top left of the screen to trigger a failsafe

- Read the full docs at [PyAutoGUI][pyautogui.readthedocs.org]
