from django.shortcuts import render, redirect
from .decorators import allowed_users, unauthenticated_user
from .models import Staff, Student, Course, Subject, Student_Leave, Students_FeedBack
from django.contrib.auth.models import User, Group
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.detail import DetailView
from django.contrib.auth.decorators import login_required
from accounts.decorators import allowed_users
from .forms import StudentFeedbackForm
from django.contrib import messages


@login_required
@allowed_users(allowed_roles=['student'])
def dashboard_view(request):

    context={
       "Hello":"Home"
    }
    return render(request, "Student/dashboard.html", context)    

@login_required
@allowed_users(allowed_roles=['student'])
def attendence_view(request):

    context = {
        "Hello":"Hello"
    }
    return render(request,"Student/attendence.html",context)

@login_required
@allowed_users(allowed_roles=['student'])
def result_view(request):

    context = {
        "Hello":"Hello"
    }
    return render(request,"Student/result.html",context)


@login_required
@allowed_users(allowed_roles=['student'])
def leave_view(request):
    student_obj = Student.objects.get(user=request.user)
    if request.method == 'POST':
        leave_date = request.POST.get('leave_date')
        message = request.POST.get('leave_message')
        leave_save = Student_Leave(student_id=student_obj, leave_date=leave_date,message=message, status=0)
        leave_save.save()
    
    
    leaves = Student_Leave.objects.filter(student_id=student_obj)
    
    context = {
        'leaves': leaves
    }
    return render(request,'Student/leave.html',context)



@login_required
@allowed_users(allowed_roles=['student'])
def feedback_view(request):
    user = request.user
    if request.method == 'POST':
        student_obj = Student.objects.get(user=user.id)
        feedback = request.POST.get('message')
        save_feedback = Students_FeedBack(student_id=student_obj, feedback=feedback, reply="")
        save_feedback.save()
    student_obj = Student.objects.get(user=user.id)
    feedbacks = Students_FeedBack.objects.filter(student_id=student_obj)
    context = {
        'feedbacks': feedbacks
    }
    return render(request,"Student/feedback.html",context)