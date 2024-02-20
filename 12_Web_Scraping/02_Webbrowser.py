# Webbrowser 

# let's use the webbrowser module to have a script
# that will call 02_Webbrowser.py 123 Main st 
# where we pass in the address of a location as the 
# second argument 

import webbrowser, sys, pyperclip

sys.argv 

# Check if command line arguments have been passed
if len(sys.argv) > 1:
    # 02_Webbrowser.py 123 Main st 
    address = ' '.join(sys.argv[1:])
    # above we want to slice out the first argument
    # ie. 02_Webbrowser.py, then join the address 
    # that's passed in with the ' '.join, so now 
    # after the slice it looks like: 123 Main st 
else:
    address = pyperclip.paste()

# https://www.google.com/maps/place/<ADDRESS>

webbrowser.open('https://www.google.com/maps/place/' + address)
