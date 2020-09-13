# ------------------------ Section 18: Working with Emails is from part 134 to 136   -----------------------------

# # # # # # # # # #  part 134 ( Advanced Dictionaries) # # # # # # # # #
# will be using SMTP library
#will try to work with GMAIL mail service

# # # # # # # # # #  part 135 ( Advanced Lists) # # # # # # # # #
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









# # # # # # # # # #  part 136 ( Advanced Lists) # # # # # # # # #