#!/usr/bin/env python
#coding=utf-8

# Import smtplib for the actual sending function
from email.mime.text import MIMEText
import smtplib
import getpass

class SendEmail(object):
    def __init__(self):
        self.address = "webmaster@latinblog.org"
        self.password = getpass.getpass()
        print("connecting")
        host = 'smtp.1and1.com:25' #SMTP host here
        self.connection = smtplib.SMTP(host)
        login_result = self.connection.login(self.address, self.password)
        print(login_result[1])

    def send(self, to_addr, subject, text):
        msg = MIMEText(text)
        msg['Subject'] = subject
        msg['From'] = self.address
        msg['To'] = to_addr
        self.connection.sendmail(self.address, to_addr, msg.as_string())
        print("email sent successfully")

    def __del__(self):
        self.connection.quit()

if __name__ == "__main__":
    s = SendEmail()
    text = "prova"
    to_addr = "matteo@latinblog.org"
    subject = "prova"

    s.send(to_addr, subject, text)
