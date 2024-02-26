# Recap

- PyAutoGUI's virtual keypresses will go to the window that has focus

- typewrite() can be passed any string of chars to type, also has an interval specifier to simulate real typing speed

- Passing a list of strings to typewrite(['shift']) lets you pass in keyboard keys

- These key specifiers can be located at print(pyautogui.KEYBOARD_KEYS)

- pyautogui.press() will press a single key once

- pyautogui.hotkey('ctrl', 'c') can be used to use hotkeys like copying, selecting, pasting etc...
