

from tkinter import messagebox

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import random
import config
import time


def spam():
    count = 0
    for row in range(0, 100):
        count += 1
        email = 'leo.mcl616@gmail.com'
        subject = 'Hi lewis'
        msg = MIMEMultipart()
        msg['From'] = config.emailAddress
        msg['To'] = email
        msg['Subject'] = subject
        body = 'From Leo x'
        msg.attach(MIMEText(body, 'plain'))

        part = MIMEBase('application', 'octet-stream')
        text = msg.as_string()
        try:
            server = smtplib.SMTP('smtp.gmail.com:587')
            server.ehlo()
            server.starttls()
            server.login(config.emailAddress, config.password)
            server.sendmail(config.emailAddress, email, text)
            server.quit()
            print('email sent')
            print(count)


        except:
            print('Email not sent')
    print(count)

spam()