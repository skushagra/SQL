from logging import exception
import mysql.connector
from mysql.connector.abstracts import TLS_V1_3_SUPPORTED
from tabulate import tabulate as tab
from sys import exit
from sendmail import sendmail
from random import randint
from time import sleep


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root"
)

c = mydb.cursor()

p = randint(111111, 999999)
c.execute('use sql_projects;')
c.execute('select email from admin where app='+'library')
data = c.fetchall()
data = data[0][0]
otp = sendmail(data, str(p))
print('OTP has been Emailed successfully.\nTime of request : '+str(otp))
utp = int(input('Enter OTP : '))
if utp != p:
    print("Incorrect Password.")
    sleep('1')
    exit()
print('\nKushagraS Liabrary Management [Version 1.0α]\n(c) KushagraS. All rights reserved.\nWelcome to the Library.\n')



while True:
    print("\nChoose command : \n1. Show Books\n2. Show Students\n3. Issue Book\n4. Accept Book\n5. Add Book\n6. Remove Book\n7. Add student\n8. Remove Student\n9. Search student\n0. Exit\n")
    i = input('Your Choice : ')

    if i=='1':
        c.execute("use sql_projects;")
        c.execute("select * from books;")
        data = c.fetchall()
        print(tab(data))
    
    if i=='2':
        c.execute("use sql_projects;")
        c.execute("select * from students;")
        data = c.fetchall()
        print(tab(data))
    
    if i=='3':
        c.execute("use sql_projects;")
        book_name = input('Enter name of book : ')
        stu_id = input('Enter student ID : ')
        c.execute('select issued_book from students where student_id='+stu_id)
        data = c.fetchall()
        data = str(data[0][0])
        if data!='N/A':
            print("\nStudent already has : "+data)
            continue
        c.execute('select * from students where student_id='+stu_id)
        data = c.fetchall()
        if data == [] or data == '':
            print('Student not found.')
            continue
        c.execute('select quantity from books where book_name="'+book_name+'"')
        quantity = c.fetchall()
        if quantity == [] or quantity == '':
            print('\nBook not found')
            continue
        quantity = int(quantity[0][0])
        quantity -= 1
        if quantity < 0:
            print('\nBook not available at the moment.')
            continue
        cmd = 'UPDATE books SET quantity='+str(quantity)+' where book_name="'+book_name+'"'
        c.execute("use sql_projects;")
        c.execute(cmd)
        cmd = 'UPDATE students SET issued_book="'+book_name+'" where student_id="'+stu_id+'"'
        c.execute(cmd)
        print("\nBook alloted successfully. Remaining copies =",str(quantity))
        mydb.commit()
    
    if i=='4':
        c.execute("use sql_projects;")
        book_name = input('Enter name of book : ')
        stu_id = input('Enter student ID : ')
        cmd = 'select issued_book from students where student_id='+stu_id
        c.execute(cmd)
        data = c.fetchall()
        data = data[0][0]
        if data != book_name:
            print('\n Student does not have the given book.')
            continue
        c.execute('select * from students where student_id='+stu_id)
        data = c.fetchall()
        if data == [] or data == '':
            print('Student not found.')
            continue
        c.execute('select quantity from books where book_name="'+book_name+'"')
        quantity = c.fetchall() 
        if quantity == [] or quantity == '':
            print('Book not found')
            continue
        quantity = quantity[0][0]
        quantity += 1
        if quantity < 0:
            print('Book not available.')
            continue
        cmd = 'UPDATE books SET quantity='+str(quantity)+' where book_name="'+book_name+'"'
        c.execute("use sql_projects;")
        c.execute(cmd)
        cmd = 'UPDATE students SET issued_book="" where student_id="'+stu_id+'"'
        c.execute(cmd)
        print("\nBook accepted successfully. Available copies =",str(quantity))
        mydb.commit()

    if i=='5':
        c.execute('use sql_projects;')
        print('Enter the following information to add a book :- ')
        book_name = input('Enter book name : ')
        writer = input('Enter writer name : ')
        publisher = input('Publisher name : ')
        isbn = input('Enter ISBN number : ')
        category = input('Enter category : ')
        rated = input('Book rated for : ')
        quantity = input('Enter quantity : ')

        cmd = 'INSERT INTO books (book_name, writer, publisher, isbn, category, rated, quantity) VALUES (%s, %s, %s, %s, %s, %s, %s)'
        val = list()
        val.append(book_name)
        val.append(writer)
        val.append(publisher)
        val.append(isbn)
        val.append(category)
        val.append(rated)
        val.append(quantity)
        val = tuple(val)
        c.execute(cmd, val)
        mydb.commit()
        print('\nBook '+book_name+' has been added successfully.')


    if i=='6':
        c.execute('use sql_projects;')
        isbn = input('\nBook ISBN number : ')
        c.execute('select book_name from books where isbn="'+isbn+'"')
        data = c.fetchall()
        data = data[0][0]
        c.execute('delete from books where isbn="'+isbn+'"')
        mydb.commit()
        print('\nBook '+data+' removed successfully.')
    
    if i=='7':
        c.execute('use sql_projects;')
        print('Enter the following information to add a book :- ')
        stname = input('Enter student name : ')
        school = input('School name : ')
        cmd = 'INSERT INTO students (student_name, school) VALUES (%s, %s)'
        val = list()
        val.append(stname)
        val.append(school)
        val = tuple(val)
        c.execute(cmd, val)
        mydb.commit()
        print('\nStudent has been added successfully.')


    if i=='8':
        c.execute('use sql_projects;')
        stid = input('\nStudent ID : ')
        c.execute('select student_name from students where student_id='+stid)
        data = c.fetchall()
        data = data[0][0]
        c.execute('delete from students where student_id='+stid)
        mydb.commit()
        print('\nBook '+data+' removed successfully.')

    if i=='9':
        search_by = ''
        print("""Search by :- 
        1. Student ID
        2. Student Name
        3. School
        4. Issued Book\n""")
        val = input('\tYour Choice : ')
        if val=='1':
            sid = input('Student ID : ')
            cmd = 'select * from students where student_id='+sid
            c.execute("use sql_projects;")
            c.execute(cmd)
            data = c.fetchall()
            if data==[] or data=="":
                print('Student not found.')
                continue
            else:
                print(tab(data))


        if val=='2':
            sid = input('Student name : ')
            cmd = 'select * from students where student_name="'+sid+'"'
            c.execute("use sql_projects;")
            c.execute(cmd)
            data = c.fetchall()
            if data==[] or data=="":
                print('Student not found.')
                continue
            else:
                print(tab(data))
        
        if val=='3':
            sid = input('School name : ')
            cmd = 'select * from students where school="'+sid+'"'
            c.execute("use sql_projects;")
            c.execute(cmd)
            data = c.fetchall()
            if data==[] or data=="":
                print('Student not found.')
                continue
            else:
                print(tab(data))

        
        if val=='4':
            sid = input('Book name : ')
            cmd = 'select * from students where issued_by="'+sid+'"'
            c.execute("use sql_projects;")
            c.execute(cmd)
            data = c.fetchall()
            if data==[] or data=="":
                print('Student not found.')
                continue
            else:
                print(tab(data))
        if val=='0':
            continue

    if i=='0':
        mydb.commit()
        mydb.close()
        break

    if i=='sql -p -f '+str(otp):
        print('\nKushagraS Library Full Power SQL Command Line\n(c) KushagraS. All Rights Reserved.\nChanges will not be comitted until you exit.')
        while True:
            cmd = input('kssql>')
            if cmd=='exit':
                mydb.commit()
                break
            try:
                c.execute(cmd)
            except:
                raise Exception('\nSQL Error. Check your syntax and try again.\n') 