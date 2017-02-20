import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.multipart import MIMEBase
import mimetypes
from email.mime.image import MIMEImage
from email.encoders import encode_base64
import time
import os

# send without attachment
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

# get attachment
def getAttachment(attachmentFilePath):
    contentType, encoding = mimetypes.guess_type(attachmentFilePath)
    if contentType is None or encoding is not None:
        contentType = 'application/octet-stream'
    mainType, subType = contentType.split('/', 1)
    file = open(attachmentFilePath, 'rb')
    if mainType == 'text':
        attachment = MIMEBase(mainType, subType)
        attachment.set_payload(file.read())
        encode_base64(attachment)
    elif mainType == 'image':
        attachment = MIMEImage(file.read())
    else:
        attachment = MIMEBase(mainType, subType)
        attachment.set_payload(file.read())
        encode_base64(attachment)
    file.close()
    attachment.add_header('Content-Disposition', 'attachment', filename=os.path.basename(attachmentFilePath))
    return attachment


# send with attachment
def sendmail_163_attachment(receiver, subject, body, attachmentFilePath):
    host = 'smtp.163.com'
    port = 25
    sender = 'm13911350399@163.com'
    authcode = 'Matao2012'

    # msg = MIMEText(body, 'html')
    msg = MIMEMultipart()
    msg['subject'] = subject
    msg['from'] = sender
    msg['to'] = ",".join(receiver)
    msg.attach(MIMEText(body, 'html'))
    msg.attach(getAttachment(attachmentFilePath))

    server = smtplib.SMTP(host,port)
    server.login(sender, authcode)
    server.sendmail(sender, receiver, msg.as_string())
    print("ok")
    server.close()

# main
getdate = time.strftime("%Y%m%d")
Title = "风险管理日报 - 资产管理事业部 - %s" % getdate
Content = open("D:\\html\\email_risk_report_format.html", 'rb').read().decode('gb2312')
attachment = "D:\\report\\风险管理日报_%s.doc" % getdate
# print(Content)
sendmail_163_attachment(['26455604@qq.com'], Title, Content, attachment)

