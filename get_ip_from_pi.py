#-*-coding:utf-8-*-
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr

import socket
import time
import urllib
from email import encoders
from email.header import Header
from email.utils import parseaddr,formataddr
from email.mime.text import MIMEText

my_sender='739281139@qq.com'    # 发件人邮箱账号
my_pass = 'kljasklefjecejaslkdfjatwwttkadfdubcji'    # 发件人邮箱密码(当时申请smtp给的口令)
my_user='739281139@qq.com'      # 收件人邮箱账号，我这边发送给自己
def mail():
    ret=True
    try:
        #获取ip地址     
        s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        s.connect(("1.1.1.1",80))
        ip_adress=s.getsockname()[0]
        s.close()
        #邮件内容
        msg=MIMEText('主人，我的IP是:'+ip_adress+'，要记牢哦','plain','utf-8')
        msg['From']=formataddr(["何群群~",my_sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
        msg['To']=formataddr(["何群群~",my_user])      # 括号里的对应收件人邮箱昵称、收件人邮箱账号
        msg['Subject']="我的树莓派ip地址"               # 邮件的主题，也可以说是标题
        
        server=smtplib.SMTP_SSL("smtp.qq.com", 465)  # 发件人邮箱中的SMTP服务器，端口是465
        server.login(my_sender, my_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码
        server.sendmail(my_sender,[my_user,],msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.quit()# 关闭连接
    except Exception:# 如果 try 中的语句没有执行，则会执行下面的 ret=False
        ret=False
    return ret

ret=mail()
if ret:
    print("邮件发送成功")
else:
    print("邮件发送失败")

