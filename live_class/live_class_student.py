from logging import setLoggerClass
import mysql.connector
import time
from sendmail import sendmail
from random import randint

print('\nWelcome to Live Class Student Attendance.\nKushagraS Version[0.1] \n(c) KushagraS. All Rights Reserved.\n')

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root"
)

c = mydb.cursor()

c.execute('use sql_projects')


flag = ''
tn = input('Enter Unique Attendance Register : ')
otp = input('Enter OTP : ')
cmd = 'select otp from live_class where uar="'+tn+'"'
c.execute(cmd)
data = c.fetchall()
if data == []:
    print('\nClass not found. Login again with proper credentials.\n')
    time.sleep(2)
else:
    data = data[0][0]
    ntop = data
    if data!=int(otp):
        print('Incorrect OTP. Login again to with correct OTP.')
        time.sleep(2)   
    else:
        print('\nLogin Successful.')
        cmd = 'select class_name from live_class where uar="'+tn+'"'
        cmd2 = 'select instructor from live_class where uar="'+tn+'"'
        c.execute(cmd)
        data = c.fetchall()
        c.execute(cmd2)
        data2 = c.fetchall()
        data2 = data2[0][0]
        data = data[0][0]
        email = input('Enter your email : ')
        join_time = time.time()
        ndt = 'You have joined class : '+data+' hosted by : '+data2
        print('You have joined class : '+data+' hosted by : '+data2)
        print('\nType exit to exit the class.')
        exit = input('\nlcsa>')
        if exit=='exit':
            print('\nExiting application')
            otp = input('Enter OTP : ')
            if int(otp) == int(ntop):
                leave_time = time.time()
                print('\nExit successful.\n')
                print('Email = '+email)
                print('Join time = '+ str(join_time))
                print('Leave time = '+ str(leave_time))
                print('Duration = '+str((leave_time-join_time)))
                cmd = 'select start_time, end_time from live_class where uar="'+tn+'"'
                c.execute(cmd)
                data = c.fetchall()
                st = float(data[0][0])
                lt = float(data[0][1])
                duration = (lt-st)*100
                data=duration*60
                print(data)
                print('Percentage time present = '+str(((leave_time-join_time)/data)*100))
                if (leave_time-join_time) >= 0.75*int(data):
                    flag = 'Present'
                    print('You are marked Present.')
                else:
                    flag = 'Absent'
                    print('You are marked absent')
                cmd= 'insert into '+tn+' (email, join_time, leave_time, poa) VALUES (%s, %s, %s, %s)'
                ls = list()
                ls.extend([email, join_time, leave_time, flag[0]])
                c.execute(cmd, ls)
                mydb.commit()
                mydb.close()
                sendmail(email, flag, ndt, str(join_time), str(leave_time), str((leave_time-join_time)), str(((leave_time-join_time)/data)*100))
                print('\nLogout Successful.')
                time.sleep(2)
