import smtplib
import getpass

smtp_obj = smtplib.SMTP('smtp.gmail.com', 587)
print(smtp_obj.ehlo())
print(smtp_obj.starttls())

email = getpass.getpass('Email: ')
password = getpass.getpass('Password: ') # bikin appp password dari google account
print(smtp_obj.login(email, password))

from_addr = email
to_addr = email
subject = input('Subject: ')
message = input('Message: ')
msg = 'Subject: ' + subject + '\n' + message
print(smtp_obj.sendmail(from_addr, to_addr, msg))
print(smtp_obj.quit())
