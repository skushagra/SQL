import smtplib, ssl
import os
import datetime
import subprocess
from mysql.connector.utils import make_abc

def sendmail(email, flag,  ndt, join_time, leave_time, duration ,dp):
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    receiver_email = email
    semail = os.environ.get('email')
    spassword = os.environ.get('pass')
    current_time = str(datetime.datetime.now())
    message = "Subject: "+ndt+"\n"
    message += "You have successfully marked your attendance for the class. Check your stats below. If you have any question, send it as a reply to this email\n\n\n"
    message += 'Join Time Index = '+str(join_time)+'\n'
    message += 'Leave Time Index = '+str(leave_time)+'\n'
    message += 'Duration  = '+str(duration)+'\n'
    message += 'Percentage of class attended = '+str(dp)+'\n'
    message += '\n\nYou are marked as '+flag+' for the class.'
    message += '\n\nYou have to record atleast 75% of the total class to be marked as present.\nExluding any extension, pre and post Start and End time of the class.'
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(semail, spassword)
        server.sendmail(semail, receiver_email, message)
    return current_time


def sendpass(email, message):
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
    ns = 'Your password for you LCMA login is '+message+'\n Use "reset -p" command to reset your password.\nThe OTP is valid only for login on : '+current_time+"\n"+"\nHere is the information of system you are logging into :- "
    message = "Subject: LCMA OTP\n"
    message += ns
    message += cnt
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(semail, spassword)
        server.sendmail(semail, receiver_email, message)
    return current_time