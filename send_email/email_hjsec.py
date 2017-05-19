# -*- coding=utf-8 -*-

import smtplib
from email.mime.text import MIMEText
import logging
import time
import os
import shutil
from email.mime.multipart import MIMEMultipart
from email.mime.multipart import MIMEBase
import mimetypes
from email.mime.image import MIMEImage
from email.encoders import encode_base64


# attachment
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

# "to_addr_list" separated by comma
def sendemail_hjsec(to_addr_list, subject, body, attachmentFilePath):
    mailserver = "mail.huajingsec.com"
    from_addr = "taoma@huajingsec.com"
    sender_password = "Huajingsec@2017"

    svr = smtplib.SMTP(mailserver, 465)
    # svr.set_debuglevel(1)
    svr.starttls()
    svr.docmd("HELO server")
    svr.login(from_addr, sender_password)

    msg = MIMEMultipart()
    msg['subject'] = subject
    msg['from'] = from_addr
    msg['to'] = ",".join(to_addr_list)
    msg.attach(MIMEText(body, 'html'))
    msg.attach(getAttachment(attachmentFilePath))

    svr.sendmail(from_addr, to_addr_list, msg.as_string())
    svr.close()

# Get date
date = time.strftime('%Y-%m-%d', time.localtime(time.time()))

# log file
log_file_name = "D:\\temp\\email_%s.log" % date
log_bak_folder = "D:\\temp\\log_bak"
if os.path.exists(log_file_name):
    if not os.path.exists(log_bak_folder):
        os.mkdir(log_bak_folder)
    shutil.copy(log_file_name, log_bak_folder)
    f = open(log_file_name, 'w')
    f.truncate()
    f.close()

# Define logging
logger = logging.getLogger('LOG')
logger.setLevel(logging.INFO)
fh = logging.FileHandler(log_file_name)
fh.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
logger.addHandler(fh)
log_content_header = "Email Sending"
logger.info(30 * "-" + log_content_header + 30 * "-")


# Compile email
date_of_title = time.strftime("%Y%m%d")
title = "风险管理日报 - 资产管理事业部 - %s" % date_of_title
content = open("D:\\html\\email_risk_report_format.html", 'rb').read().decode('gb2312')
recipient = ['taoma@huajingsec.com']
attachment = "E:\\风控合规\\风控日报\\风险管理日报_%s.doc" % date_of_title

# main
try:
    sendemail_hjsec(recipient,title, content, attachment)
    logger.info("Successfully sent to %s" % recipient)
    logger.info("Attachment is %s" % attachment)
except Exception as error:
    logger.exception(error)



