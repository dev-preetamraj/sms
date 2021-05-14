from django.shortcuts import render, redirect
from .decorators import allowed_users, unauthenticated_user
from .models import Staff, Student, Course, Subject, Student_Leave
from django.contrib.auth.models import User, Group
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.detail import DetailView


def student_home_view(request):

    context={
       "Hello":"Home"
    }
    return render(request, "Student/student_home.html", context)    

def student_view_attendence_view(request):

    context = {
        "Hello":"Hello"
    }
    return render(request,"Student/student_view_attendence.html",context)

def student_result_view(request):

    context = {
        "Hello":"Hello"
    }
    return render(request,"Student/student_result.html",context)

def student_apply_leave_view(request,pk):
    student_obj = Student.objects.get(id = pk)
    leave_data = Student_Leave.object.filter(student_id=student_obj)
    context = {
        "leave_data": leave_data
    }
    return render(request,'Student/student_apply_leave.html',context)




def student_send_feedback_view(request):

    context = {
        "Hello":"Hello"
    }
    return render(request,"Student/student_send_feedback.html",context)