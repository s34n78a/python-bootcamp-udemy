import imaplib
import getpass
import email

M = imaplib.IMAP4_SSL('imap.gmail.com')

email_addr = getpass.getpass('Email: ')
password = getpass.getpass('Password: ') # bikin appp password dari google account
print(M.login(email_addr, password))

print(M.list())
print(M.select('inbox'))

typ, data = M.search(None, 'SUBJECT "test kirim email pake python"')
print(typ)
print(data)

email_id = data[0]
result, email_data = M.fetch(email_id, '(RFC822)')
print(result)
print(email_data)

raw_email = email_data[0][1]
print(raw_email)
raw_email_str = raw_email.decode('utf-8')
print(raw_email_str)

email_message = email.message_from_string(raw_email_str)
print(email_message)

for part in email_message.walk():
    if part.get_content_type() == "text/plain":
        body = part.get_payload(decode=True)
        print(body)
    else:
        continue
