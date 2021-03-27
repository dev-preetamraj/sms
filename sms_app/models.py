from django.db import models
from django.contrib.auth.models import User


class Course(models.Model):
    course_name = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.course_name


class Subject(models.Model):
    subject_name = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.subject_name


class Staff(models.Model):
    user = models.OneToOneField(
        User, null=True, blank=True, on_delete=models.CASCADE)
    course_teach = models.ManyToManyField(Course, null=True, blank=True)
    subject_teach = models.ManyToManyField(Subject, null=True, blank=True)

    def __str__(self):
        return self.user.username
