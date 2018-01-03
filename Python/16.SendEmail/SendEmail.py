#!/usr/bin/python

import smtplib

sender =  'vesna1@on.net.mk' #'test@mail.net.mk';
receivers = ['golemkroasan@gmail.com'];

message = """From: From Person <test@mail.net.mk>
To: To Person <malin@mail.net.mk>
Subject: SMTP e-mail test

This is a test e-mail message.
"""

try:
   #setup mail server
   smtpObj = smtplib.SMTP('217.16.70.1')
   
   #send message
   smtpObj.sendmail(sender, receivers, message)         
   
   #print success
   print("Successfully sent email");
except SMTPException:
   print("Error: unable to send email");