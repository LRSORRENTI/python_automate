# Checking Emails

# You can check emails using the: 
# NOTE IMAP(Internet Message Access Protocol)

# Python does have an imap module but it's 
# a little complicated to use easily, instead we'll 
# use two third party modules called imapclient, and 
# pyzmail

import imapclient 

# setup the connection using imapclient method, and 
# padd in two args, first is the domain name, the 
# second is ssl=True, which is for Secure Socket Layer
conn = imapclient.IMAPClient('imap.outlook.com', ssl=True)

conn.login('Youremail@outlook.com', '123123')

conn.select('INBOX', readonly=True)
# Pass in the inbox name, ane set readonly to true 
# to read emails only

UIDS = conn.search(['SINCE 20-Aug-2023'])
# search has special syntax, the above returns all 
# emails since august of 2023

# the above returns [47416, 47417, 47428,..... many more]

# To actually use those UIDS call the fetch method: 

# The first argument is a list with the UID. and 
# the second arg is which parts of the email we want
rawMessage = conn.fetch([47416], ['BODY[]', 'FLAGS'])

# import pyzmail

# message = pyzmail.PyzMessage.factory(rawMessage[47416][b'BODY[]'])

# message.getSubject()
# 'so long...' 

# message.get_addresses('from')
# [(Youremail@outlook.com, Youremail@outlook.com)]