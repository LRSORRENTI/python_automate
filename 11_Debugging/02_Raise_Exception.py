'''
*****************
*               *
*               *
*               *
*****************
'''

# Let's define a function that will create boxes,
# like the one above

def boxPrint(symbol, width, height):
    if len(symbol) != 1:
        raise Exception('"symbol" needs to be a string of length 1 ')
    if (width < 2) or (height < 2):
        raise Exception('"Width & Height must be greater than 2')
    print(symbol * width)
    for i in range(height - 2):
        print(symbol + (' ' * (width - 2)) + symbol)
    print(symbol * width)

boxPrint('|', 15, 5)

# |||||||||||||||
# |             |
# |             |
# |             |
# |||||||||||||||

boxPrint('=', 5, 7)
# =====
# =   =
# =   =
# =   =
# =   =
# =   =
# =====

# boxPrint('--', 15, 5)
# line 14, in boxPrint
#     raise Exception('"symbol" needs to be a string of length 1 ')     
# Exception: "symbol" needs to be a string of length 1

# The above is known as a traceback

# You can also use the traceback module to return a 
# string of the traceback error:

import traceback
try: 
    raise Exception('This is an error')
except:
    errorFile = open('error_log.txt', 'a')
    errorFile.write(traceback.format_exc())
    errorFile.close()
    print('The traceback info was written to error_log.txt')