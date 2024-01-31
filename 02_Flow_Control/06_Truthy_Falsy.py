print('enter a name')
name = input()
if name != '': 
    print('thanks for entering you name' + ' ' + name)
else: 
    print('you did not enter a name')

print(bool(name))