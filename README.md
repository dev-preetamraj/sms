# School Management System
The School Management System is a sleek web-based application to manage the record of students and teachers.
With this system,school administration can easily manage students' and teachers details i.e., results, attendance, courses,feeadback.
Their are 3 roles in the webapp HoD, Staff, Student. HoD have all rights to access the application. They can add/delete students form the record

  
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
