# ------------------------ Section 18: Working with Emails is from part 134 to 136   -----------------------------

# # # # # # # # # #  part 134 ( Introduction to Emails with Python) # # # # # # # # #
# will be using SMTP library
#will try to work with GMAIL mail service

# # # # # # # # # #  part 135 ( Sending Emails with Python) # # # # # # # # #
""" 
import smtplib

smtp_object = smtplib.SMTP('smtp.gmail.com',587) #this is the protcols that big mail comapnies are using
#465 this is another port or do not add any port
# check the virus defender on the local machine which will stop running you script , in case

#
smtp_object.ehlo() # establish a connection
# print(smtp_object.ehlo()) # establish a connection
# the correct reponse will look like
#(250, b'smtp.gmail.com at your service, [83.248.137.187]\nSIZE 35882577\n8BITMIME\nSTARTTLS\nENHANCEDSTATUSCODES\nPIPELINING\nCHUNKING\nSMTPUTF8')


# smtp_object.starttls() # if we are using 587 port means we are using TLS encryption
# if not that means you are using ssl and do not need this statement

smtp_object.starttls()
# print(smtp_object.starttls())
#THE CORRECT RESPONSE : 220, b'2.0.0 Ready to start TLS'

### do not save a password in script , it will be accessible to every body.
# do not use user input, which is visible also

##### generate an application password to GMAIL and activate 2-pass verification
import getpass
email = getpass.getpass('Email please: ')
password = getpass.getpass('Password please: ')
print(email+'\n'+password)
smtp_object.login(email,password) # you should notice the respone will be {} which mean SUCSESSFUL LOGIN


#calling send method
from_adress = getpass.getpass('Enter your email: ')
to_adress = getpass.getpass('Enter recipents email adress: ')
subject = input('Enter the subject')
message = input('Enter content of your email')
msg = 'Subject: ' + subject + '\n' + message
smtp_object.sendmail(from_adress,to_adress,msg)


# now you need to close the connection
smtp_object.quit()
#(221, b'2.0.0 closing connection j1sm22376227pgq.33 - gsmtp') should be the response
"""


# # # # # # # # # #  part 136 (Receiving Emails with Python) # # # # # # # # #
# we will deal with Imaplibrary and email library
import imaplib
import  email
import  getpass

M = imaplib.IMAP4_SSL('imap.gmail.com')

email = getpass.getpass('Email please: ')
password = getpass.getpass('Password please: ')
print(M.login(email,password))

print(M.list())
M.select("Sent")
# M.select("inbox")

# Searching Mail
# Now that we have connected to our mail, we should be able to search for it using the specialized syntax of IMAP. 
# Here are the different search keys you can use:
#-------------------------------------------------------------------------------------------------------------------------------
# Keyword	                                                    Definition
# 'ALL'	                                                        Returns all messages in your email folder. Often there are size limits from imaplib. To change these use imaplib._MAXLINE = 100 , where 100 is whatever you want the limit to be.
# 'BEFORE date'	                                                Returns all messages before the date. Date must be formatted as 01-Nov-2000.
# 'ON date'         	                                        Returns all messages on the date. Date must be formatted as 01-Nov-2000.
# 'SINCE date'      	                                        Returns all messages after the date. Date must be formatted as 01-Nov-2000.
# 'FROM some_string '	                                        Returns all from the sender in the string. String can be an email, for example 'FROM user@example.com' or just a string that may appear in the email, "FROM example"
# 'TO some_string'  	                                        Returns all outgoing email to the email in the string. String can be an email, for example 'FROM user@example.com' or just a string that may appear in the email, "FROM example"
# 'CC some_string' and/or 'BCC some_string'                     Returns all messages in your email folder. Often there are size limits from imaplib. To change these use imaplib._MAXLINE = 100 , where 100 is whatever you want the limit to be.
# 'SUBJECT string','BODY string','TEXT "string with spaces"'	Returns all messages with the subject string or the string in the body of the email. If the string you are searching for has spaces in it, wrap it in double quotes.
# 'SEEN', 'UNSEEN'	                                            Returns all messages that have been seen or unseen. (Also known as read or unread)
# 'ANSWERED', 'UNANSWERED'	                                    Returns all messages that have been replied to or unreplied to.
# 'DELETED', 'UNDELETED'	                                    Returns all messages that have been deleted or that have not been deleted.

# Use if you get an error saying limit was reached
imaplib._MAXLINE = 10000000
typ ,data = M.search(None,'SUBJECT "Python test"')

print(typ)
print(data)
result, email_data = M.fetch(data[0],"(RFC822)")
raw_email = email_data[0][1]
raw_email_string = raw_email.decode('utf-8')

email_message = email.message_from_string(raw_email_string)

for part in email_message.walk():
    if part.get_content_type() == "text/plain":
        body = part.get_payload(decode=True)
        print(body)