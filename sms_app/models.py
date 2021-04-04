from django.db import models
from django.contrib.auth.models import User
# from django.contrib.auth.models import AbstractUser




# Overriding the Default Django Auth User and adding One More Field (user_type)


# class CustomUser(AbstractUser):
#     user_type_data = ((1, "HOD"), (2, "Staff"), (3, "Student"))
#     user_type = models.CharField(
#         default=1, choices=user_type_data, max_length=10)


# HOD_TABLE(HOD id,user,address,date_joined,last login)
class HODTable(models.Model):
    id = models.AutoField(primary_key = True)
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    address = models.TextField(null = True)
    date_joined = models.DateField(auto_now_add = True)
    date_updated = models.DateField(auto_now = True)

    def __str__(self):
        return "@{}".format(str(self.user.username))

# STAFF_TABLE(Staff id,user,address,date_joined,last login)
class Staff(models.Model):
    id = models.AutoField(primary_key = True)
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    profile_pic = models.ImageField(default = "", null = True, blank = True)
    address = models.TextField(null = True)
    date_joined = models.DateField(auto_now_add = True)
    last_login = models.DateField(auto_now = True)

    def __str__(self):
        return "@{}".format(str(self.user.username))

# SessionYear_TABLE(session id, start date, end date)
class SessionYear(models.Model):
    id = models.AutoField(primary_key = True)
    session_start_year = models.DateField()
    session_end_year = models.DateField()

    def __str__(self):
        return "{} : {}".format(str(self.session_start_year), str(self.session_end_year))

# Student_table(student id, user, gender, address, profile_pic, sessionid <- foreignky of SessionYear table,
#                 course id <- Foreign key referencing to Course Table, date joined, last login )
class Student(models.Model):
    id = models.AutoField(primary_key = True)
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    GENDER = (('Male', 'Male'),('Female', 'Female'),('Other', 'Other'))
    gender = models.CharField(max_length = 10, choices = GENDER)
    address = models.TextField(null = True)
    profile_pic = models.ImageField(default = "", null = True, blank = True)
    session_under = models.ForeignKey(
        SessionYear, on_delete = models.CASCADE, null = True, blank = True)
    courses_taken = models.ForeignKey(
        'Course', on_delete = models.DO_NOTHING, null = True, blank = True)
    date_joined = models.DateField(auto_now_add = True)
    last_login = models.DateField(auto_now = True)

    def __str__(self):
        return "@{}".format(str(self.user.username))

# Course_TABLE(course id,user,address, date_created, lastupdate)
class Course(models.Model):
    id = models.AutoField(primary_key = True)
    course_name = models.CharField(max_length = 100)
    date_created = models.DateField(auto_now_add = True)
    date_updated = models.DateField(auto_now = True)

    def __str__(self):
        return self.course_name

# Subject_TABLE(subject id, subject name, Course id <- Foreign key referencing to course table, 
#               staff id <- Forign key referencing to staff table, date_created, lastupdate)
class Subject(models.Model):
    id = models.AutoField(primary_key = True)
    subject_name = models.CharField(max_length = 100)
    under_course = models.ForeignKey(Course, on_delete = models.CASCADE)
    taught_by = models.ForeignKey(
        Staff, on_delete=models.CASCADE, null = True, blank = True)
    date_created = models.DateField(auto_now_add = True)
    date_updated = models.DateField(auto_now = True)

    def __str__(self):
        return self.subject_name


# Attendence Table(attendence id, subject id <- Foregin key referencing to subject table, date of attendence, 
#                   session year id <- Foreign key referencing to session year table, date created, date updated)
class Attendance(models.Model):
    id = models.AutoField( primary_key=True )
    subject_id = models.ForeignKey(Subject, on_delete=models.CASCADE)
    attendance_date = models.DateField()
    session_year_id = models.ForeignKey(SessionYear, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.attendence_date)

# students Attendence Table(id, attendence id <- Foregin key referencing to attendence table, attendence type i.e Present or Absent 
#                   student id <- Foreign key referencing to student table, date created, date updated)
class StudentAttendance(models.Model):
    id = models.AutoField(primary_key=True)
    attendance_id = models.ForeignKey(Attendance, on_delete=models.CASCADE)
    student_id = models.ForeignKey(Students, on_delete=models.CASCADE) 
    attendence_type = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.attendence_type)

