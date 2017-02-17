#-*- encoding: gb2312 -*-
import os, sys, string
import smtplib
import base64


# 邮件服务器地址
mailserver = "mail.huajingsec.com"
# 邮件用户名
username = "taoma"
# 密码
password = "Huajingsec@2017"
# smtp会话过程中的mail from地址
from_addr = "taoma@huajingsec.com"
# smtp会话过程中的rcpt to地址
to_addr = "taoma@huajingsec.com"
# 信件内容
msg = "This is a test"
svr = smtplib.SMTP(mailserver)
# 设置为调试模式，就是在会话过程中会有输出信息
svr.set_debuglevel(1)
# ehlo命令，docmd方法包括了获取对方服务器返回信息，如果支持安全邮件，返回值里会有starttls提示
svr.docmd("EHLO server")
svr.starttls()
# auth login 命令
svr.docmd("EHLO server")
svr.docmd("AUTH LOGIN")
# 发送用户名，是base64编码过的，用send发送的，所以要用getreply获取返回信息
svr.send(base64.b64encode(username.encode(encoding='utf-8')))
svr.send('\r\n')
svr.getreply()
# 发送密码
svr.send(base64.b64encode(password.encode(encoding='utf-8')))
svr.send('\r\n')
svr.getreply()
# mail from, 发送邮件发送者
svr.docmd("MAIL FROM: <%s>" % from_addr)
# rcpt to, 邮件接收者
svr.docmd("RCPT TO: <%s>" % to_addr)
# data命令，开始发送数据
svr.docmd("DATA")
# 发送正文数据
svr.send(msg)
# 比如以 . 作为正文发送结束的标记
svr.send(" . ")
svr.send('\r\n')
svr.getreply()
# 发送结束，退出
svr.quit()