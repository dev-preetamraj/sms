from django.shortcuts import render, redirect
from .decorators import allowed_users, unauthenticated_user
from .models import Staff, Student, Course, Subject, Student_Leave
from django.contrib.auth.models import User, Group
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.detail import DetailView


def dashboard_view(request):

    context={
       "Hello":"Home"
    }
    return render(request, "Student/dashboard.html", context)    

def attendence_view(request):

    context = {
        "Hello":"Hello"
    }
    return render(request,"Student/attendence.html",context)

def result_view(request):

    context = {
        "Hello":"Hello"
    }
    return render(request,"Student/result.html",context)

def leave_view(request):
    #student_obj = Student.objects.get(id = pk)
    #leave_data = Student_Leave.object.filter(student_id=student_obj)
    context = {
        "leave_data": "leave_data"
    }
    return render(request,'Student/leave.html',context)




def feedback_view(request):

    context = {
        "Hello":"Hello"
    }
    return render(request,"Student/feedback.html",context)