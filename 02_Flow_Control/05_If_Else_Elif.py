# If statements are often occompanied by else 
# blocks to give an alternate flow: 

password = 'swordfish'

if password == 'swordfish':
    print('Access granted')
else: 
    print('Access Denied')

# There is also elif, which can be used before the 
# else to check for addtional conditions before the 
# final else 

passwordTwo = 'admi'

if passwordTwo == 'swordfish':
    print('access granted')
elif passwordTwo == 'admin':
    print('access granted to admin')
else: 
    print('no access')