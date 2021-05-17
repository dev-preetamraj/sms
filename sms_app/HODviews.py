from django.shortcuts import render, redirect
from .decorators import allowed_users, unauthenticated_user
from .models import Staff, Student, Course, Subject
from django.contrib.auth.models import User, Group
from .forms import AddStaffForm, RegisterUserForm, AddStudentForm, UpdateUserForm, AddCourseForm, AddSubjectForm, AddSessionForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.views.generic.detail import DetailView
from accounts.decorators import allowed_users



def admin_dashboard(request):
    students = Student.objects.all()
    student_count = students.count()
    staffs = Staff.objects.all()
    staff_count = staffs.count()
    context = {
        'student_count': student_count,
        'staff_count': staff_count
    }
    return render(request, 'HOD/dashboard.html', context)



def hod_dashboard(req):
    students = Student.objects.all()
    student_count = students.count()
    staffs = Staff.objects.all()
    staff_count = staffs.count()
    courses = Course.objects.all()
    course_count = courses.count()
    subjects = Subject.objects.all()
    subject_count = subjects.count()
    context = {
        'student_count': student_count,
        'staff_count': staff_count,
        'course_count': course_count,
        'subject_count': subject_count
    }
    return render(req, "HOD/hod_dashboard.html", context)



def register_user_view(request):
    form = RegisterUserForm()
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            user_save = form.save()
            if form.cleaned_data.get('user_type') == 'hod':
                set_group = Group.objects.get(name='hod')
                user_save.groups.add(set_group)
            elif form.cleaned_data.get('user_type') == 'staff':
                set_group = Group.objects.get(name='staff')
                user_save.groups.add(set_group)
            else:
                set_group = Group.objects.get(name='student')
                user_save.groups.add(set_group)
            return redirect('admin_dashboard')
        else:
            return redirect('register_user')
    context = {'form': form}
    return render(request, 'accounts/add_user.html', context)


def charts_view(req):
    context = {}
    return render(req, 'HOD/charts.html', context)



def manage_student_view(request):
    students = Student.objects.all()

    context = {
        'students': students,

    }
    return render(request, 'HOD/manage_student.html', context)


def manage_staff_view(request):
    staffs = Staff.objects.all()

    context = {
        'staffs': staffs,
    }
    return render(request, 'HOD/manage_staff.html', context)



def manage_courses_view(request):
    courses = Course.objects.all()
    context = {
        'courses': courses
    }
    return render(request, 'HOD/manage_courses.html', context)



def add_course_view(request):
    form = AddCourseForm()
    if request.method == 'POST':
        form = AddCourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('manage_courses_view')

    context = {
        'form': form
    }
    return render(request, 'HOD/add_course.html', context)



def manage_subjects_view(request):
    context = {}
    return render(request, 'HOD/manage_subjects.html', context)



def add_subjects_view(request):
    form = AddSubjectForm()
    if request.method == 'POST':
        form = AddSubjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('manage_subjects_view')
    context = {
        'form': form
    }
    return render(request, 'HOD/add_subjects.html', context)


def add_session_view(request):
    form = AddSessionForm()
    if request.method == 'POST':
        form = AddSessionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('manage_sessions_view')
    context = {
        'form': form
    }
    return render(request, 'HOD/add_session.html', context)





def manage_sessions_view(request):
    context = {}
    return render(request, 'HOD/manage_sessions.html', context)



def view_attendance(request):
    context = {}
    return render(request, 'HOD/view_attendance.html', context)



def staff_feedback_view(request):
    context = {}
    return render(request, 'HOD/staff_feedback.html', context)



def students_feedback_view(request):
    context = {}
    return render(request, 'HOD/students_feedback.html', context)



def staff_leave_view(request):
    context = {}
    return render(request, 'HOD/staff_leave.html', context)



def student_leave_view(request):
    context = {}
    return render(request, 'HOD/students_leave.html', context)



def login_view(req):
    context = {}
    return render(req, 'HOD/login.html', context)


def test_view(request):
    context = {}
    return render(request, 'HOD/test.html', context)


def tables_view(request):
    context = {}
    return render(request, 'HOD/tables.html', context)



def add_student_view(request):
    form = AddStudentForm()
    form.fields['user'].queryset = User.objects.filter(groups__name='student')
    if request.method == 'POST':
        form = AddStudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('manage_student_view')
    context = {
        'form': form
    }
    return render(request, 'HOD/add_student.html', context)



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
    return render(request, 'HOD/update_student.html', context)



def delete_student_view(request, pk):
    students = Student.objects.get(id=pk)
    if request.method == "POST":
        students.user.delete()
        return redirect('manage_student_view')
    context = {'item': students}
    return render(request, 'HOD/delete_student.html', context)



def see_detail_view(request, pk):
    stu = Student.objects.get(id=pk)

    context = {'student': stu}
    return render(request, 'HOD/see_detail.html', context)



def add_staff_view(request):
    form = AddStaffForm()
    if request.method == 'POST':
        form = AddStaffForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('manage_staff_view')
    context = {
        'form': form
    }
    return render(request, 'HOD/add_staff.html', context)



def update_staff_view(request, pk):
    staffs = Staff.objects.get(id=pk)
    staff_form = AddStaffForm(instance=staffs)
    user_form = UpdateUserForm(instance=staffs.user)
    if request.method == 'POST':
        staff_form = AddStaffForm(request.POST, request.FILES, instance=staffs)
        user_form = UpdateUserForm(request.POST, instance=staffs.user)
        if staff_form.is_valid() and user_form.is_valid():
            staff_form.save()
            user_form.save()
            return redirect('manage_staff_view')
    context = {
        'user_form': user_form,
        'staff_form': staff_form
    }
    return render(request, 'HOD/update_staff.html', context)



def delete_staff_view(request, pk):
    staffs = Staff.objects.get(id=pk)
    if request.method == "POST":
        staffs.user.delete()
        return redirect('manage_staff_view')
    context = {'item': staffs}
    return render(request, 'HOD/delete_staff.html', context)



def see_detail_staff_view(request, pk):
    sta = Staff.objects.get(id=pk)
    context = {'staff': sta}
    return render(request, 'HOD/see_detail_staff.html', context)



def result_view(request):
    context = {}
    return render(request, 'HOD/result.html', context)
