#-*- encoding: gb2312 -*-
import os, sys, string
import smtplib
import base64

# �ʼ���������ַ
mailserver = "mail.huajingsec.com"
# �ʼ��û���
username = "huajingsec.com\\taoma"
# ����
password = "Huajingsec@2017"
# smtp�Ự�����е�mail from��ַ
from_addr = "taoma@huajingsec.com"
# smtp�Ự�����е�rcpt to��ַ
to_addr = "taoma@huajingsec.com"
# �ż�����
msg = "my test mail"

# adding part
type1msg = "NTLMSSP2+ HJ_AM_BJ_DP008huajingsec.com"


svr = smtplib.SMTP(mailserver)
# ����Ϊ����ģʽ�������ڻỰ�����л��������Ϣ
svr.set_debuglevel(1)
# ehlo���docmd���������˻�ȡ�Է�������������Ϣ�����֧�ְ�ȫ�ʼ�������ֵ�����starttls��ʾ
svr.docmd("EHLO server")
svr.starttls()
# auth login ����
svr.docmd("EHLO server")
type1msg_encode = base64.b64encode(type1msg.encode(encoding='utf-8'))
svr.docmd("AUTH NTLM")
svr.send(type1msg_encode)
# �����û�������base64������ģ���send���͵ģ�����Ҫ��getreply��ȡ������Ϣ
svr.send(base64.b64encode(username.encode(encoding='utf-8')))
svr.getreply()
# ��������
svr.send(base64.b64encode(password.encode(encoding='utf-8')))
svr.getreply()
# mail from, �����ʼ�������
svr.docmd("MAIL FROM: <%s>" % from_addr)
# rcpt to, �ʼ�������
svr.docmd("RCPT TO: <%s>" % to_addr)
# data�����ʼ��������
svr.docmd("DATA")
# ������������
svr.send(msg)
# ������ . ��Ϊ���ķ��ͽ����ı��
svr.send(" . ")
svr.getreply()
# ���ͽ������˳�
svr.quit()