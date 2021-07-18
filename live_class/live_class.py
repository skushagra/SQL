import datetime
import random
from tabulate import tabulate as tba
from mysql.connector.utils import intstore
import mysql.connector
from sys import exit
from sendmail import sendmail, sendpass


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root"
)

c = mydb.cursor()

c.execute('use sql_projects')


c.execute('select email from admin where app="live_class" or app="live class"')
data = c.fetchall()
data = data[0][0]

pastoch = randint(111111,999999)
sendpass(data, pastoch)
pas = input('OTP : ')
if pas != pastoch:
    print('Incorrect Password.')
    exit()


print('\nWelcome to Live Class Management.\nKushagraS Version[0.1] \n(c) KushagraS. All Rights Reserved.\n')

while True:
    print('Select an appropriate command : \n\t1. Create new class\n\t2. Retrive old class data.\n\t3. Stop attendance for a class\n')
    ch = input('Your choice : ')
    if ch=='1':
        print('Creating new class : \n')
        class_name = input('\tClass name : ')
        date = str(datetime.date.today())
        description = input('\tDescribe the class : ')
        instructor = input('\tInstructor : ')
        start = input('\tStart time (in 24 hour format) : ')
        end = input('\tEnd time (in 24 hour format) : ')
        duration = float(end)-float(start)
        otp = random.randint(111111, 999999)
        uar = ''
        MAX_LIMIT = 122
        for _ in range(10):
            random_integer = random.randint(97, MAX_LIMIT)       
            # Keep appending random characters using chr(x)
            uar += (chr(random_integer))
        print('\nNew Class Information\n')
        lsa = list()
        lsa.append(class_name)
        lsa.append(date)
        lsa.append(description)
        lsa.append(instructor)
        lsa.append(start)
        lsa.append(end)
        lsa.append(otp)
        lsa.append(duration*100)
        lsa.append(uar)
        ls = list()
        ls.append(lsa)
        print(tba(ls, headers=["Class Name", "Date", "Description", "Isntructor", "Start Time", "End Time", "OTP", "Duration(min)", "Unique Attendance Register"]), '\n\n')
        lsa.remove(duration*100)
        print('\nShare the OTP and Unique Attendance Register to mark attendance.\n')
        cmd = 'INSERT INTO live_class(class_name, class_date, description, instructor, start_time, end_time, otp, uar) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)'
        c.execute(cmd, lsa)
        mydb.commit()
        print('Class created successfully.')
        c.execute('select class_id from live_class where class_date="'+date+'" and otp='+str(otp))
        id = c.fetchall()
        id = id[0][0]
        cmd = 'CREATE TABLE '+uar+'(email varchar(50) not null, join_time varchar(20) not null, leave_time varchar(20) not null, poa varchar(1) not null ,PRIMARY KEY ( email ));'
        c.execute(cmd)
        print('\nAttendance table',uar,'created successfully.\n')
        print('Student email will be added to table : '+uar+'\n')
        mydb.commit()
    
    if ch=='2':
        c.execute('select * from live_class;')
        data = c.fetchall()
        print(tba(data, headers=["Class Name", "Date", "Description", "Isntructor", "Start Time", "End Time", "OTP", "Class ID", "Unique Attendance Register"]))
        print('\n\n')
        cho = input('Enter class ID : ')
        cmd = 'select uar from live_class where class_id='+cho
        c.execute(cmd)
        data = c.fetchall()
        if data ==[] or data=='':
            print('Class not found.')
        else:
            data = data[0][0]
            cmd = 'select * from '+data
            c.execute(cmd)
            data = c.fetchall()
            if data == [] or data == '':
                print('No attendance has been marked for this class.\n')
            else:
                print('\n'+tba(data, headers=["Email", "Join Time", "Leave Time", "P || A"]))
    
    if ch=='3':
        c.execute('select * from live_class;')
        data = c.fetchall()
        print(tba(data, headers=["Class Name", "Date", "Description", "Isntructor", "Start Time", "End Time", "OTP", "Duration(min)", "Unique Attendance Register"]))
        print('\n\n')
        cho = input('Enter class ID : ')
        notp = random.randint(111111,999999)
        cmd = 'update live_class set OTP='+str(notp)+' where class_id='+cho
        c.execute(cmd)
        mydb.commit()
        print('OTP has been changend. Attendance will not not be marked using old OTP.\n')


    if ch=='exit':
        mydb.commit()
        mydb.close()
        exit()
    
    if ch=='sql -p -f':
        print('\nKushagraS Live Class Full Power SQL Command Line\n(c) KushagraS. All Rights Reserved.\nChanges will not be comitted until you exit.\n\n')
        while True:
            cmd = input('kssql>')
            if cmd=='exit':
                mydb.commit()
                break
            c.execute(cmd) 
            data = c.fetchall()
            print(tba(data))
