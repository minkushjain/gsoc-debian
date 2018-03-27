import requests
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

print("Welcome to GSoC 2018")
print("Project: Wizard/GUI Helping Students get Started\n")
print("This is a program to automate the process of subscription to the mailing list.\n")

with requests.Session() as c:
    url="https://lists.debian.org/cgi-bin/subscribe.pl"
    email=input("Enter you E-mail: ")
    c.get(url)
    login_data={'user_email':email, 'list':'debian-outreach', 'action':'Subscribe'}
    c.post(url,data=login_data,stream=True)
    print("\nCheck your mail for further instructions!")

#confirming subscription by replying to the mail:
    
a=input("\nEnter the code of the subject you recieved in your mail: ")
b="CONFIRM "+a
fromaddr=" "  # Enter sender's email address
toaddr="debian-outreach-request@lists.debian.org"
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = b
 
body = "Subscribe"
msg.attach(MIMEText(body, 'plain'))
 
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, " ")    #Enter password of sender's email in " "
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()
print("\nCongrats, your email has been successfully registered in the mailing list!")
k=input("\nPress any key to exit")
