import smtplib
from email.mime.text import MIMEText

def sendmail_exchange(receiver, subject, body):
    host = 'mail.huajingsec.com'
    port = 25
    sender = 'taoma@huajingsec.com'
    authcode = 'Huajingsec@2017'
    msg = MIMEText(body, 'html')
    msg['subject'] = subject
    msg['from'] = sender
    msg['to'] = receiver
    server = smtplib.SMTP(host,port)
    server.starttls()
    server.login(sender, authcode)
    server.sendmail(sender,receiver,msg.as_string())
    print("ok")

sendmail_exchange('26455604@qq.com','Plan','Hi, Please ack me')

