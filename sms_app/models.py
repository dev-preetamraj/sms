from django.db import models
from django.contrib.auth.models import User
# from django.contrib.auth.models import AbstractUser


class SessionYear(models.Model):
    id = models.AutoField(primary_key=True)
    session_start_year = models.DateField()
    session_end_year = models.DateField()

    def __str__(self):
        return "{} : {}".format(str(self.session_start_year), str(self.session_end_year))

# Overriding the Default Django Auth User and adding One More Field (user_type)


# class CustomUser(AbstractUser):
#     user_type_data = ((1, "HOD"), (2, "Staff"), (3, "Student"))
#     user_type = models.CharField(
#         default=1, choices=user_type_data, max_length=10)


class HODTable(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.TextField(null=True)
    date_joined = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)

    def __str__(self):
        return "@{}".format(str(self.user.username))


class Staff(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.TextField(null=True)
    date_joined = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)

    def __str__(self):
        return "@{}".format(str(self.user.username))


class Student(models.Model):
    GENDER = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=10, choices=GENDER)
    address = models.TextField(null=True)
    profile_pic = models.ImageField(default="", null=True, blank=True)
    session_under = models.ForeignKey(
        SessionYear, on_delete=models.DO_NOTHING, null=True, blank=True)
    courses_taken = models.ForeignKey(
        'Course', on_delete=models.DO_NOTHING, null=True, blank=True)
    date_joined = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)

    def __str__(self):
        return "@{}".format(str(self.user.username))


class Course(models.Model):
    name = models.CharField(max_length=100)
    date_created = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)

    def __str__(self):
        return self.name


class Subject(models.Model):
    name = models.CharField(max_length=100)
    under_course = models.ForeignKey(Course, on_delete=models.DO_NOTHING)
    taught_by = models.ForeignKey(
        Staff, on_delete=models.DO_NOTHING, null=True, blank=True)
    date_created = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)

    def __str__(self):
        return self.name
