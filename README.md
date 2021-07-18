<html>
<body>
<h1>SQL Applications and Database Management</h1>
  <h2>Liabray Management</h2>
  <p>Liabray Management aims at managing books and students at the same time.</p>
  <p>Registered members can add and delete students, books. Also issue and accept books. The application is password protected, a six digit number is generated randomly and sent to a registered email for the application.</p>
  <p>Upon login the admin can exxecute the following commands : </p>
</body>
</html>

```
  - See available books.
  - See registered students.
  - Issue Book.
  - Accept book.
  - Add Book.
  - Remove Book.
  - Add Student.
  - Remove Student.
  - Search Student
  - Exit
```

<html>
<body>
  <p>The application is also packed with full power SQL terminal which can run all SQL commands. The changes however for safety reasons are not comitted until exit. The function og the above mention commands is similar to what they are named. The application is terminal based and is equiped with features which can cause major security and logical errors.</p>
</body>
</html>

<html>
<body>
  <br><br>
  <h2>Live Class Atendance</h2>
  <p>The application is designed to accept and keep record of atudents attending a class.</p>
  <p>This application is more like an idea of how GUI based live class applications can keep a record of students attending the class. A teacher creates a class using the <b>live_class.py</b> application which gives generates a six digit OTP and a Unique Attendance Register(UAR). The UAR and the OTP is shared with student whic logins to the <b>live_class_student.py</b> application and if correct authentication is provided the student is logged in successfully. <br><br>
    
The student submits his/her email and their time of attendance is calculated henceforth. When the student wishes to exit or the class ends, the student is asked for the OTP again. If the final verification is successful the student successfully exits the class and the leave time is recorded. The duration for which the student attended the class is calculated and (by default) if it is more than 75% of the duration of the class the student is marked present else absent. All data is stired and can be referenced in future until deleted manually.<br><br>
Student is emailed the following information once he/she exits the class :
</p>
</body>
</html>
```
- Join Time Index : Number of seconds since epoch while joining
- Leave Time Index : Number of seconds since epoch while leaving
- Duration : Time student was in the class in seconds
- Percentage of class attended : (Duration/Duration of class)*100
- Attendance status : Present or Absent
- A short descripitive text
```


#### Here is a sample of the email sent : 
![image](https://user-images.githubusercontent.com/66439372/126080489-bd63c3aa-1707-4082-932b-9f8d10156b79.png)
