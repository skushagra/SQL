import smtplib, ssl
import os
import datetime
import subprocess

def sendmail(email, message):
    Id = subprocess.check_output(['systeminfo']).decode('utf-8').split('\n')
    new = []
    cnt = ''
    # arrange the string into clear info
    for item in Id:
	    new.append(str(item.split("\r")[:-1]))
    for i in new:
	    cnt += (i[2:-2])+"\n"
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    receiver_email = email
    semail = os.environ.get('email')
    spassword = os.environ.get('pass')
    current_time = str(datetime.datetime.now())
    ns = 'Your password for you DBS login is '+message+'\n Use "reset -p" command to reset your password.\nThe OTP is valid only for login on : '+current_time+"\n"+"\nHere is the information of system you are logging into :- "
    message = "Subject: DBS OTP\n"
    message += ns
    message += cnt
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(semail, spassword)
        server.sendmail(semail, receiver_email, message)
    return current_time
