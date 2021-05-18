from django.shortcuts import render, redirect
from .decorators import allowed_users, unauthenticated_user
from django.contrib.auth.models import User, Group
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.detail import DetailView
from django.contrib.auth.decorators import login_required
from accounts.decorators import allowed_users
from .models import Staff_Leave, Staffs_FeedBack, Staff

@login_required
@allowed_users(allowed_roles=['staff'])
def staff_dashboard(req):
    context = {}
    return render(req, 'Staff/dashboard.html', context)

@login_required
@allowed_users(allowed_roles=['staff'])
def take_attendance(req):
    context = {}
    return render(req, 'Staff/take_attendance.html', context)

@login_required
@allowed_users(allowed_roles=['staff'])
def view_attendance(req):
    context = {}
    return render(req, 'Staff/view_attendance.html', context)

@login_required
@allowed_users(allowed_roles=['staff'])
def add_result(req):
    context = {}
    return render(req, 'Staff/add_result.html', context)

@login_required
@allowed_users(allowed_roles=['staff'])
def leave(request):
    staff_obj = Staff.objects.get(user=request.user.id)
    staff_leaves = Staff_Leave.objects.filter(staff_id=staff_obj)
    context = {
        "staff_leaves": staff_leaves
    }
    return render(request, 'Staff/leave.html', context)

@login_required
@allowed_users(allowed_roles=['staff'])
def staff_leave_save(request):
    if request.method == 'POST':
        staff_obj = Staff.objects.get(user=request.user.id)
        leave_date = request.POST.get('leave_date')
        message = request.POST.get('leave_message')
        staff_leave_save = Staff_Leave(staff_id=staff_obj, leave_date=leave_date, message=message, status=0)
        staff_leave_save.save()
        return redirect('leaveStaff')

@login_required
@allowed_users(allowed_roles=['staff'])
def feedback(request):
    staff_obj = Staff.objects.get(user=request.user.id)
    feedback_data = Staffs_FeedBack.objects.filter(staff_id=staff_obj)
    context = {
        "feedbacks": feedback_data
    }
    return render(request, 'Staff/feedback.html', context)


@login_required
@allowed_users(allowed_roles=['staff'])
def save_staff_feedback(request):
    user = request.user
    if request.method == 'POST':
        staff_obj = Staff.objects.get(user=user.id)
        feedback = request.POST.get('message')
        save_feedback = Staffs_FeedBack(staff_id = staff_obj, feedback = feedback, reply = "")
        save_feedback.save()
        return redirect("feedbackStaff")

