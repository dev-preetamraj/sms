from django.contrib import admin
from .models import SessionYear, HODTable, Staff, Student, Course, Subject, Attendance, StudentAttendance, Staffs_FeedBack, Students_FeedBack, Staff_Leave, Student_Leave, Result

admin.site.register(HODTable)
admin.site.register(Staff)
admin.site.register(SessionYear)
admin.site.register(Student)
admin.site.register(Course)
admin.site.register(Subject)
admin.site.register(Attendance)
admin.site.register(StudentAttendance)
admin.site.register(Staffs_FeedBack)
admin.site.register(Students_FeedBack)
admin.site.register(Staff_Leave)
admin.site.register(Student_Leave)
admin.site.register(Result)
