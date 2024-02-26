# Controlling the keyboard with python:

import pyautogui

# The typewrite method sends keypresses to the computer 

# NOTE It's impotant to know that the keypresses 
# go to whichever field or window has focus,
# you may need to use 
# pyautogui.moveTo(x=822,y=30, duration=5)
# pyautogui.click(x=822,y=30)
# then once the above clicks into the field, it's 
# good to start typing 

# But you can also use a semi colon to execute two 
# lines :

pyautogui.click(x=200, y=200, duration=0.2) ; pyautogui.typewrite('hello world', interval=0.1)

# You can pass in values to move the cursor left or right 
# using a list of chars and keywords like 'left' ,'right
pyautogui.click(x=200, y=200, duration=0.2) ; pyautogui.typewrite(['a', 'b', 'left', 'left', 'X', 'Y' ], interval=0.1)
# print(pyautogui.KEYBOARD_KEYS)

# To press a single key, like f12 or any key use any of 
#  06_ControlKeyboard.py 
# ['\t', '\n', '\r', ' ', '!', '"', '#', '$', '%',
# '&', "'", '(', ')', '*', '+', ',', '-', '.', '/',
# '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
# ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']',
# '^', '_', '`', 'a', 'b', 'c', 'd', 'e', 'f', 'g',
# 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
# 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|',
# '}', '~', 'accept', 'add', 'alt', 'altleft',
# 'altright', 'apps', 'backspace', 'browserback',
# 'browserfavorites', 'browserforward', 'browserhome',
# 'browserrefresh', 'browsersearch', 'browserstop',
# 'capslock', 'clear', 'convert', 'ctrl', 'ctrlleft',
# 'ctrlright', 'decimal', 'del', 'delete', 'divide',
# 'down', 'end', 'enter', 'esc',
# 'escape', 'execute', 'f1', 'f10', 'f11', 'f12',
# 'f13', 'f14', 'f15', 'f16', 'f17', 'f18', 'f19',
# 'f2', 'f20', 'f21', 'f22',
# 'f23', 'f24', 'f3', 'f4', 'f5', 'f6', 'f7',
# 'f8', 'f9', 'final', 'fn', 'hanguel', 'hangul',
# 'hanja', 'help', 'home', 'insert', 'junja', 'kana',
# 'kanji', 'launchapp1', 'launchapp2',
# 'launchmail', 'launchmediaselect', 'left', 'modechange', 'multiply',
# 'nexttrack', 'nonconvert', 'num0', 'num1', 'num2',
# 'num3', 'num4', 'num5', 'num6', 'num7', 'num8',
# 'num9', 'numlock', 'pagedown', 'pageup', 'pause', 'pgdn',
# 'pgup', 'playpause', 'prevtrack', 'print',
# 'printscreen', 'prntscrn', 'prtsc', 'prtscr',
# 'return', 'right', 'scrolllock', 'select',
# 'separator', 'shift', 'shiftleft', 'shiftright',
# 'sleep', 'space', 'stop',
# 'subtract', 'tab', 'up', 'volumedown', 'volumemute',
# 'volumeup', 'win', 'winleft', 'winright', 'yen',
# 'command', 'option', 'optionleft', 'optionright']

# You can also specify hotkey like 'ctrl + a',
# 'ctrl + c', 'ctrl + v' 

pyautogui.hotkey('ctrl', 'o')
pyautogui.hotkey('ctrl', 'a')