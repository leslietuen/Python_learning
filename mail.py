#!bin/env python
#-*- coding:utf-8 -*-
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr,formataddr
import smtplib

from_addr = '2296649254@qq.com'
passwd = 'YYYLYMcfslrq0804'
to_addr = 'pureord@gmail.com'
smtp_addr="smtp.qq.com"
port = '25'
def _format_addr(s):
	name,addr = parseaddr(s)
	return formataddr((Header(name,'utf-8').encode(),addr))
msg = MIMEText('Hello','plain','utf-8')
msg['From'] = _format_addr('Sender<%s>' % from_addr)
msg['To'] = _format_addr('receive<%s>' % to_addr)
msg['Subject'] = Header('subject','utf-8').encode()

s = smtplib.SMTP(smtp_addr,25)
s.set_debuglevel(1)
s.login(from_addr,passwd)
s.sendmail(from_addr,to_addr,msg.as_string())
s.quit()
