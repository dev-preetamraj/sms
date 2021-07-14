# School Management System
The School Management System is a sleek web-based application to manage the record of students and teachers.
The objective of the “School Management System” is to design a scheduling system for an education center.  There will be three main actors of the application 1) Admin 2) Student 3) Faculty.

Admin can manage student records, the Attendance record of the students, Subject details ETC. Admin can add new records as well as can view and delelte the details of all the records.

Faculty/Teachers/Staff can add attendance, Subject, and mark sheet, as well as they can view the record for the same.

 A student can view the mark sheet can check the attendance details fees details and subject details.

One can access the webapp from below link:
https://prp-sms.herokuapp.com/

  
## Available Scripts

1. First fork this repo and then Clone it
2. Run `cd sms` - to move into the directory 
3. Install virtualenv using command - `pip install virtualenv`
3. Now activate the virtual environment using command - `virtualenv env`
4. Now activate the virtual env using command - `.\env\Scripts\activate` . This will activate the virtual environment. For linux and Mac try - `source env/bin/activate`
5. Install all requirements by - `pip install -r requirements.txt`.
7. Now to migrate the models run - `python manage.py migrate`.
8. Now to activate the localhost server run - `python manage.py runserver`<br />
<pre>
	Runs the app in the development mode.<br />
	Open (http://localhost:8000) to view it in the browser.
</pre>
