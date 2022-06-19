import smtplib
import main
import creds as cd

# Email Information
sent_from = cd.gmail_user
to = ['calvinjmin@gmail.com']
subject = 'Automated Email'
body = main.percent_change['TSLA']

# Email Template
email_text = """\
From: %s
To: %s
Subject: %s

%s
""" % (sent_from, ", ".join(to), subject, body)

try:
    # STMP Connect
    smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    smtp_server.ehlo()

    smtp_server.login(cd.gmail_user, cd.gmail_password)
    
    smtp_server.sendmail(sent_from, to, email_text)
    smtp_server.close()
    
    print ("Email sent successfully!")
except Exception as ex:
    print ("Something went wrong….",ex)

