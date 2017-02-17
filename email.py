import smtplib
from email.mime.text import MIMEText

mailserver = "mail.huajingsec.com"
to_addr = "taoma@huajingsec.com"
from_addr = "taoma@huajingsec.com"

# Content
body = "hello email"
subject = "Test"
msg = MIMEText(body, 'html')
msg['subject'] = subject
msg['from'] = from_addr
msg['to'] = to_addr

svr = smtplib.SMTP(mailserver,465)
svr.set_debuglevel(1)
svr.starttls()
svr.docmd("HELO server")

# Auth
username = "taoma@huajingsec.com" # not work
password = "Huajingsec@2017"
svr.login(username, password)

# send
svr.sendmail(from_addr,to_addr,msg.as_string())

