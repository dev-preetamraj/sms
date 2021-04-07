from django.shortcuts import render, redirect
from .decorators import allowed_users, unauthenticated_user
from .models import Staff, Student
from .forms import AddStaffForm, RegisterUserForm


def admin_dashboard(request):
    students = Student.objects.all()
    student_count = students.count()
    staffs = Staff.objects.all()
    staff_count = staffs.count()
    context = {
        'student_count': student_count,
        'staff_count': staff_count
    }
    return render(request, 'main/dashboard.html', context)


def register_user_view(request):
    form = RegisterUserForm()
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_dashboard')
        else:
            return redirect('register_user')
    context = {'form': form}
    return render(request, 'accounts/add_user.html', context)


def add_staff(request):
    form = AddStaffForm()
    if request.method == 'POST':
        form = AddStaffForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_dashboard')
        else:
            return redirect('add_staff')

    context = {'form': form}
    return render(request, 'app/add_staff.html', context)

def charts_view(req):
    context = {}
    return render(req, 'main/charts.html', context)

def tables_view(request):
    students = Student.objects.all()

    context = {
        'students': students,
   
    }
    return render(request, 'main/tables.html', context)
def login_view(req):
    context = {}
    return render(req, 'main/login.html', context)

def test_view(request):
    context = {}
    return render(request, 'main/test.html', context)
