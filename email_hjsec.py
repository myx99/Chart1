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
username = "taoma@huajingsec.com"
password = "Huajingsec@2017"
svr.login(username, password)

# send
svr.sendmail(from_addr,to_addr,msg.as_string())

def sendemail_hjsec(receiver, subject, body):
    mailserver = "mail.huajingsec.com"
    sender = "taoma@huajingsec.com"
    sender_password = "Huajingsec@2017"
    svr = smtplib.SMTP(mailserver, 465)
    svr.starttls()
    svr.docmd("HELO server")
    svr.login(sender, sender_password)
    msg = MIMEText(body, 'html')
    msg['subject'] = subject
    msg['from'] = from_addr
    msg['to'] = to_addr
    svr.sendmail(sender, receiver, msg.as_string())


