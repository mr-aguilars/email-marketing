import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'jose@aol.com'
email['to'] = 'yourname@yourdomain.com'
email['subject'] = 'You won 1,000,000 dollars!'

email.set_content(html.substitute(name= 'Tin'), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
	smtp.ehlo()
	smtp.starttls()
	smtp.login('yourname@email.com', 'yourpassword1234') #Login info goes here
	smtp. send_message(email)
	print('all good boss!')
