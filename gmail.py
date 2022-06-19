import smtplib
import main
import creds as cd

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

msg = MIMEMultipart('alternative')

# Email Information
msg['Subject'] = "STOCKS TODAY - %s" % (main.today)
msg['From'] = cd.gmail_user
msg['To'] = "calvinjmin@gmail.com"

html = """\
<html>
  <head></head>
  <body>
    <p style="color: green;">DATE: %s</p>
    <h3>End Price</h3>
    <p>%s</p>

    <h3>Percent Change - Day </h3>
    <p>%s</p>

    <h3>Percent Change - Week </h3>
    <p>%s</p>

    <h3>Percent Change - Month </h3>
    <p>%s</p>
</body>
</html>
""" % ( main.today , main.end_price,  main.percent_change["day"], main.percent_change["week"], main.percent_change["month"])

htmlText= MIMEText(html, 'html')
msg.attach(htmlText)

try:
    # STMP Connect
    smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    smtp_server.ehlo()

    smtp_server.login(cd.gmail_user, cd.gmail_password)
    
    smtp_server.sendmail(msg['From'], msg['To'], msg.as_string())
    smtp_server.close()
    
    print ("Email sent successfully!")
except Exception as ex:
    print ("Something went wrong….",ex)

