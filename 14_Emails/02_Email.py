import smtplib 

# the smtp lib exposes a method SMTP, the first 
# argument is the name of the email server, like
# .gmail, .yahoo, .outlook, and the second argument 
# is the port for emails, usually 587
conn = smtplib.SMTP('smtp-mail.outlook.com', 587)

# To start the connection, you first need to call 
# the method ehlo()
conn.ehlo()

# Next the conn returns a tuple, the first is a status 
# code, 250 for good connect, and the second is a large 
# bytes object, that can look like a long string

# Then since we've connected, we need to add tls 
# encryption layer:

conn.starttls()

# Then pass the username and pw for the account:
conn.login('youremailhere@outlook.com', '23123')

# After login call the sendmail function, the first
# argument is the from address, the second is 
# the target address

# The third argument can be long, since the entire body 
# needs to be crammed into sendmails third argument:

conn.sendmail('youremailhere@outlook.com', \
               'asweigart@gmail.com', \
                'Subject: Test SMTP With Python... \n\n \
                Dear Al, thanks for the awesome course on Python! \
                \n\n -Luke'  )
# The return value for sendmail is a dictionary, 
# if it was successful it will return an empty
# dictionary, however if any emails failed to send, 
# it will be inside the dictionary

# Then call .quit to disconnect from the SMTP server
conn.quit()

# NOTE some providers like gmail require a specific 
# password for accessing an account through third 
# parties, like a python script, you need to configure 
# on on their webapp, and if you need to send more than 
# a few emails, it's better to find a commercial 
# emailing service 