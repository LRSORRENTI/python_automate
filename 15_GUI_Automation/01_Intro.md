# GUI Automation

Significant amounts of automation can be utilized with actual keyboard and mouse controls, think about repetetive tasks you click, and press through daily, some of these repetetive presses and clicks could be automated with Python

Almost like programming a robotic arm, that can move the mouse and click for you

## PyAutoGUI

We'll use a third party package to help us transform repetetive clicks and presses into single automated processes

# IMPORTANT NOTE:

Automating mouse functions, can sometimes lead to unwanted mouse behavior if a bug or some kind of loop error occurs, as a failsafe, if you mis-program something, try to slam the mouse to the top left corner of the screen quickly, this pyautogui package
has a failsafe if the mouse touches the very top and left of the screen, it exits the program:

raise FailSafeException(
pyautogui.FailSafeException: PyAutoGUI fail-safe triggered from mouse moving to a corner of the screen. To disable this fail-safe, set pyautogui.FAILSAFE to False. DISABLING FAIL-SAFE IS NOT RECOMMENDED.)
