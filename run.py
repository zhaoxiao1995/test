# tests = [Test_zhihu_demo("test_zhihu01"),Test_zhihu_demo("test_zhihu02_text"),Test_zhihu_demo('test_zhihu03_')]
# suite = unittest.TestSuite()
# suite.addTests(tests)

from bao import HTMLTestRunner
import time
import unittest

#============添加用例到htmltestrunner去执行=====
suite = unittest.defaultTestLoader.discover(start_dir='./cases',pattern='Lux*.py') #把用例添加变量中 去这个文件夹中搜索learn开头.py结尾的文件
reportname = time.strftime('%Y-%m-%d-%H-%M-%S-') #把当前时间赋给变量
with open("./reports/%s测试报告.html" % reportname,"wb") as zx: #把这个变量加入到文件名中 wb是w的二进制 把文件名赋给zx
    runner = HTMLTestRunner.HTMLTestRunner(stream=zx, verbosity=2,title="测试报告",description="执行人：赵霄")
    runner.run(suite) 


from email.mime.text import MIMEText  
from email.header import Header  
import smtplib    
import os  

#==============定义发送邮件==========  
def send_mail(file_new):  #打开报告 放到邮件body中
    f = open(file_new,'rb')  
    mail_body = f.read()  
    f.close()  
  
    msg = MIMEText(mail_body,'html','utf-8')   #实例化创建邮件
    
    msg['Subject'] = Header('自动化测试报告','utf-8')# 邮件信息头 必须
    msg['From'] = "18583707821@163.com"
    msg['To'] = "1103214015@qq.com"
#==============发送模块=========
    smtp = smtplib.SMTP()  
    smtp.connect('smtp.163.com')                                      #邮箱服务器  
    smtp.login("18583707821@163.com","zx1103214015")                           #登录邮箱  
    smtp.sendmail("18583707821@163.com","1103214015@qq.com",msg.as_string()) #发送者和接收者  
    smtp.quit()  
    print("邮件已发出！注意查收。")  
  
#======查找测试目录，找到最新生成的测试报告文件======  
def new_report(test_report):  
    lists = os.listdir(test_report)                                    #列出目录的下所有文件和文件夹保存到lists  
    lists.sort(key=lambda fn:os.path.getmtime(test_report + "\\" + fn))#按时间排序  
    file_new = os.path.join(test_report,lists[-1])                     #获取最新的文件保存到file_new  
    print(file_new)  
    return file_new  

test_report = "./reports"
new_report = new_report(test_report)  
send_mail(new_report)     #发送测试报告  
  