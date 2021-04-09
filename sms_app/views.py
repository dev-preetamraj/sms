from django.shortcuts import render, redirect
from .decorators import allowed_users, unauthenticated_user
from .models import Staff, Student
from .forms import AddStaffForm, RegisterUserForm, AddStudentForm, UpdateUserForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.detail import DetailView


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


def manage_student_view(request):
    students = Student.objects.all()

    context = {
        'students': students,

    }
    return render(request, 'main/manage_student.html', context)


def login_view(req):
    context = {}
    return render(req, 'main/login.html', context)


def test_view(request):
    context = {}
    return render(request, 'main/test.html', context)


def tables_view(request):
    context = {}
    return render(request, 'main/tables.html', context)


def add_student_view(request):
    form = AddStudentForm()
    if request.method == 'POST':
        form = AddStudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('manage_student_view')
    context = {
        'form': form
    }
    return render(request, 'main/add_student.html', context)


def update_student_view(request, pk):
    students = Student.objects.get(id=pk)
    student_form = AddStudentForm(instance=students)
    user_form = UpdateUserForm(instance=students.user)
    if request.method == 'POST':
        student_form = AddStudentForm(
            request.POST, request.FILES, instance=students)
        user_form = UpdateUserForm(request.POST, instance=students.user)
        if student_form.is_valid() and user_form.is_valid():
            student_form.save()
            user_form.save()
            return redirect('manage_student_view')
    context = {
        'student_form': student_form,
        'user_form': user_form
    }
    return render(request, 'main/update_student.html', context)


def delete_student_view(request, pk):
    students = Student.objects.get(id=pk)
    if request.method == "POST":
        students.user.delete()
        return redirect('manage_student_view')
    context = {'item': students}
    return render(request, 'main/delete_student.html', context)


def see_detail_view(request, pk):
    stu = Student.objects.get(id=pk)

    context = {'student': stu}
    return render(request, 'main/see_detail.html', context)
