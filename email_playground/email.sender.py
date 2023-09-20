import smtplib
from email.message  import EmailMessage
from string import Template
from pathlib import Path

html= Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'username' #To the use/ create the email body.
email['to'] = 'random@spamthisplease.com'
email['subject'] = 'Spam text'

email.set_content(html.substitute({'name':'Bob'}),'html')  #To the user

with smtplib.SMTP(host='smtp.spamthisplease.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('spam@randomspamthisplease.com', 'xxxx') #Host address
    smtp.send_message(email)
    print('all good')

