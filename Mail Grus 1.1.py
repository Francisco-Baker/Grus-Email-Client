import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email import encoders
from email.header import Header
import time

#print title
print("Tw&py Email Client (experimental version1) by: Tianwei Li\nProtocol: SMTP")

b=0

#get user and pwd
file = open("user.txt", mode="r")
user = file.read()

file = open("pwd.txt", mode="r")
pwd = file.read()

#announce info
print("user：", user)
print("password：********")

#get specific information
a = input("py > user> command>:")

if a == "pwd":
    print("password:\n",pwd)
    time.sleep(5.0)
    exit()

if a == "num":
    a = int(input("Please input the quantity of mail:"))

if a =="ip":
    import ip
    exit()

a = int(1)

receiver = input("Please input the receiver of your mail:")
header = input("Header:")
content = input("Content:")

#conduct
for b in range(0,a):
    to = [receiver]
    msg = MIMEMultipart()
    msg['Subject'] = Header(header, 'utf-8')
    msg['From'] = Header(user)

    content1 = MIMEText(content, 'plain', 'utf-8')
    msg.attach(content1)

    s = smtplib.SMTP('smtp.sina.com')
    s.starttls()
    s.login(user, pwd)
    s.sendmail(user, to, msg.as_string())
    s.close()
    b = b+1




