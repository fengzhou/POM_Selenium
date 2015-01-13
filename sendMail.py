#coding=utf-8
'''
Created on 2014年12月19日

'''

import smtplib,time,os
from email.mime.text import MIMEText

#发送邮件
def sendMail(file_new):
    #定义发送方
    mail_From = ""
    #定义接收方
    mail_To = ""
    f = open(file_new)
    #定义正文
    mail_body = f.read()
    msg = MIMEText(mail_body,'html','utf-8')
    #定义标题
    msg['Subject'] = u'My TEST REPORT'
    #定义发送时间
    msg['date']=time.strftime('%a,%d %b %Y %H:%M:%S %Z')
    smtp = smtplib.SMTP()
    #链接SMTP服务器，此处用的是qq的smtp服务器
    smtp.connect('smtp.qq.com', 25)
    #用户名
    smtp.login(mail_From, 'mima')
    smtp.sendmail(mail_From, mail_To, msg.as_string())
    smtp.quit()

#获取最新的测试报告
def get_Report_file():
    result_dir = os.getcwd()+r"\Report"
    lists = os.listdir(result_dir)
    lists.sort(key=lambda fn: os.path.getatime(result_dir+"\\"+fn) if not 
               os.path.isdir(result_dir+"\\"+fn) else 0)
    #找到最新生成的文件
    file_new = os.path.join(result_dir,lists[-1]);
    return file_new

#发送测试报告
sendMail(get_Report_file())


    