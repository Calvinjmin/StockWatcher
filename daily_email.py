import os
import smtplib
import main
from dotenv import load_dotenv

load_dotenv()

gmail_user = os.environ.get('GOOGLE_ACCOUNT', 'example@gmail.com')
gmail_password = os.environ.get('GOOGLE_PASSWORD', 'NONE')

sent_from = gmail_user
to = ['calvinjmin@gmail.com']
subject = 'Automated Email'
body = main.bmw

# Email Template
email_text = """\
From: %s
To: %s
Subject: %s

%s
""" % (sent_from, ", ".join(to), subject, body)

try:
    smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    smtp_server.ehlo()
    smtp_server.login(gmail_user, gmail_password)
    smtp_server.sendmail(sent_from, to, email_text)
    smtp_server.close()
    print ("Email sent successfully!")
except Exception as ex:
    print ("Something went wrong….",ex)

