import smtplib
from email.mime.text import MIMEText
import time

def sendmail_163(receiver, subject, body):
    host = 'smtp.163.com'
    port = 25
    sender = 'm13911350399@163.com'
    authcode = 'Matao2012'

    msg = MIMEText(body, 'html')
    # msg = mm.MIMEMultipart()
    msg['subject'] = subject
    msg['from'] = sender
    msg['to'] = ",".join(receiver)
    # msg.attach(MIMEText(body, 'html'))

    server = smtplib.SMTP(host,port)
    server.login(sender, authcode)
    server.sendmail(sender, receiver, msg.as_string())
    print("ok")
    server.close()

getdate = time.strftime("%Y%m%d")
Title = "风险管理日报 - 资产管理事业部 - %s" % getdate
Content = open("C:\\temp\\email.html", 'rb').read().decode('utf-8')
print(Content)

sendmail_163(['26455604@qq.com','taoma@huajingsec.com'], Title, Content)

