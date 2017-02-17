import smtplib
from email.mime.text import MIMEText

def sendmail_163(receiver, subject, body):
    host = 'smtp.163.com'
    port = 25
    sender = 'm13911350399@163.com'
    authcode = 'Matao2012'
    msg = MIMEText(body, 'html')
    msg['subject'] = subject
    msg['from'] = sender
    msg['to'] = receiver
    server = smtplib.SMTP(host,port)
    server.login(sender, authcode)
    server.sendmail(sender,receiver,msg.as_string())
    print("ok")

sendmail_163('26455604@qq.com','Plan','Hi, Please ack me')

