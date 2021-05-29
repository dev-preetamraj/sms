from django.shortcuts import render, redirect
from .decorators import allowed_users, unauthenticated_user
from .models import Attendance, HODTable, SessionYear, Staff, Staff_Leave, Staffs_FeedBack, Student, Course, StudentAttendance, Student_Leave, Students_FeedBack, Subject
from django.contrib.auth.models import User, Group
from .forms import AddStaffForm, RegisterUserForm, AddStudentForm, UpdateUserForm, AddCourseForm, AddSubjectForm, AddSessionForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.views.generic.detail import DetailView
from accounts.decorators import allowed_users, hod_only
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.views.decorators.csrf import csrf_exempt


@login_required
@allowed_users(allowed_roles=['hod'])
def admin_dashboard(request):
    students = Student.objects.all()
    student_count = students.count()
    staffs = Staff.objects.all()
    staff_count = staffs.count()
    context = {
        'student_count': student_count,
        'staff_count': staff_count
    }
    if request.user.groups.filter(name='hod'):
        return render(request, 'HOD/dashboard.html', context)
    else:
        return render(request,'accounts/notallowed.html', {})


@login_required
@allowed_users(allowed_roles=['hod'])
def hod_dashboard(request):
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
    if request.user.groups.filter(name='hod'):
        return render(request, "HOD/hod_dashboard.html", context)
    else:
        return render(request,'accounts/notallowed.html', {})
        


@login_required
@allowed_users(allowed_roles=['hod'])
def register_user_view(request):
    form = RegisterUserForm()
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            user_save = form.save()
            if form.cleaned_data.get('user_type') == 'hod':
                set_group = Group.objects.get(name='hod')
                user_save.groups.add(set_group)
                gender = form.cleaned_data.get('gender')
                create_hod = HODTable(
                    user = user_save,
                    gender = gender
                )
                create_hod.save()
            elif form.cleaned_data.get('user_type') == 'staff':
                set_group = Group.objects.get(name='staff')
                user_save.groups.add(set_group)
                gender = form.cleaned_data.get('gender')
                create_staff = Staff(
                    user = user_save,
                    gender = gender,
                )
                create_staff.save()
            else:
                set_group = Group.objects.get(name='student')
                user_save.groups.add(set_group)
                gender = form.cleaned_data.get('gender')
                create_student = Student(
                    user = user_save,
                    gender = gender,
                )
                create_student.save()
                
            return redirect('register_user')
        else:
            return redirect('register_user')
    context = {'form': form}
    return render(request, 'accounts/add_user.html', context)


def charts_view(req):
    context = {}
    return render(req, 'HOD/charts.html', context)


@login_required
@allowed_users(allowed_roles=['hod'])
def manage_student_view(request):
    students = Student.objects.all()

    context = {
        'students': students,

    }
    return render(request, 'HOD/manage_student.html', context)

@login_required
@allowed_users(allowed_roles=['hod'])
def manage_staff_view(request):
    staffs = Staff.objects.all()

    context = {
        'staffs': staffs,
    }
    return render(request, 'HOD/manage_staff.html', context)


@login_required
@allowed_users(allowed_roles=['hod'])
def manage_courses_view(request):
    courses = Course.objects.all()
    context = {
        'courses': courses
    }
    return render(request, 'HOD/manage_courses.html', context)


@login_required
@allowed_users(allowed_roles=['hod'])
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


@login_required
@allowed_users(allowed_roles=['hod'])
def manage_subjects_view(request):
    subjects = Subject.objects.all()
    context = {
        'subjects' : subjects
    }
    return render(request, 'HOD/manage_subjects.html', context)




@login_required
@allowed_users(allowed_roles=['hod'])
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

@login_required
@allowed_users(allowed_roles=['hod'])
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

#  ======================   Session  ========================== #


@login_required
@allowed_users(allowed_roles=['hod'])
def manage_sessions_view(request):
    sessions = SessionYear.objects.all()
    context = {
        'sessions' : sessions
    }
    return render(request, 'HOD/manage_sessions.html', context)



@login_required
@allowed_users(allowed_roles=['hod'])
def delete_session_view(request, pk):
    session = SessionYear.objects.get(id=pk)
    if request.method == "POST":
        session.delete()
        return redirect('manage_sessions_view')
    context = {'item': session}
    return render(request, 'HOD/delete_session.html',context)


@login_required
@allowed_users(allowed_roles=['hod'])
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

@login_required
@allowed_users(allowed_roles=['hod'])
def update_session_view(request, pk):
    session = SessionYear.objects.get(id=pk)
    session_form = AddSessionForm(instance=session)
    
    if request.method == 'POST':
        session_form = AddSessionForm(
            request.POST, request.FILES, instance=session)
        if session_form.is_valid():
            session_form.save()
            return redirect('manage_sessions_view')
    context = {
        'session_form': session_form
    }
    return render(request, 'HOD/update_session.html', context)

@login_required
@allowed_users(allowed_roles=['hod'])
def view_attendance(request):
    subjects = Subject.objects.all()
    sessions = SessionYear.objects.all()
    context = {
        'subjects': subjects,
        'sessions': sessions
    }
    if request.method == 'POST':
        subject_id = request.POST.get('subject_id')
        session_id = request.POST.get('session_year_id')
        filtered_attendance = Attendance.objects.filter(subject_id=subject_id,session_year_id=session_id)
        context['filtered_attendance'] = filtered_attendance

        
        attendance_id = 0
        default_text = ""
        if request.POST.get('attendance_date')==None:
            attendance_id = 1
            default_text = "Sample Attendance Structure"
        else:
            attendance_id = request.POST.get('attendance_date')

        final_attendance_id = Attendance.objects.get(id=attendance_id).id
        student_attendance = StudentAttendance.objects.filter(attendance_id=final_attendance_id)
        student_attendance_count = False
        if student_attendance.count()==0:
            student_attendance_count = True
        context['student_attendance'] = student_attendance
        context['student_attendance_count'] = student_attendance_count
        context['default_text'] = default_text
    
    return render(request, 'HOD/view_attendance.html', context)


@login_required
@allowed_users(allowed_roles=['hod'])
def staff_feedback_view(request):
    staff_feedbacks = Staffs_FeedBack.objects.all()
    context = {
        'staff_feedbacks': staff_feedbacks
    }
    return render(request, 'HOD/staff_feedback.html', context)

@csrf_exempt
@login_required
@allowed_users(allowed_roles=['hod'])
def staff_feedback_message_reply(request):
    feedback_id = request.POST.get('id')
    feedback_reply = request.POST.get('reply')

    try:
        feedback = Staffs_FeedBack.objects.get(id=feedback_id)
        feedback.reply = feedback_reply
        feedback.save()
        return HttpResponse("True")

    except:
        return HttpResponse("False")


@login_required
@allowed_users(allowed_roles=['hod'])
def students_feedback_view(request):
    student_feedbacks = Students_FeedBack.objects.all()
    context = {
        'student_feedbacks': student_feedbacks
    }
    return render(request, 'HOD/students_feedback.html', context)


@csrf_exempt
@login_required
@allowed_users(allowed_roles=['hod'])
def student_feedback_message_reply(request):
    feedback_id = request.POST.get('id')
    feedback_reply = request.POST.get('reply')

    try:
        feedback = Students_FeedBack.objects.get(id=feedback_id)
        feedback.reply = feedback_reply
        feedback.save()
        return HttpResponse("True")

    except:
        return HttpResponse("False")

@login_required
@allowed_users(allowed_roles=['hod'])
def staff_leave_view(request):
    leaves = Staff_Leave.objects.all()
    context = {
        'leaves': leaves
    }
    return render(request, 'HOD/staff_leave.html', context)

@login_required
@allowed_users(allowed_roles=['hod'])
def staff_leave_approve(request, leave_id):
    leave = Staff_Leave.objects.get(id=leave_id)
    leave.status = 1
    leave.save()
    return redirect('staff_leave_view')

@login_required
@allowed_users(allowed_roles=['hod'])
def staff_leave_reject(request, leave_id):
    leave = Staff_Leave.objects.get(id=leave_id)
    leave.status = 2
    leave.save()
    return redirect('staff_leave_view')


@login_required
@allowed_users(allowed_roles=['hod'])
def student_leave_view(request):
    leaves = Student_Leave.objects.all()
    context = {
        'leaves': leaves
    }
    return render(request, 'HOD/students_leave.html', context)

@login_required
@allowed_users(allowed_roles=['hod'])
def student_leave_approve(request, leave_id):
    leave = Student_Leave.objects.get(id=leave_id)
    leave.status = 1
    leave.save()
    return redirect('student_leave_view')

@login_required
@allowed_users(allowed_roles=['hod'])
def student_leave_reject(request, leave_id):
    leave = Student_Leave.objects.get(id=leave_id)
    leave.status = 2
    leave.save()
    return redirect('student_leave_view')


def login_view(req):
    context = {}
    return render(req, 'HOD/login.html', context)


def test_view(request):
    context = {}
    return render(request, 'HOD/test.html', context)


def tables_view(request):
    context = {}
    return render(request, 'HOD/tables.html', context)





@login_required
@allowed_users(allowed_roles=['hod'])
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


@login_required
@allowed_users(allowed_roles=['hod'])
def delete_student_view(request, pk):
    students = Student.objects.get(id=pk)
    if request.method == "POST":
        students.user.delete()
        return redirect('manage_student_view')
    context = {'item': students}
    return render(request, 'HOD/delete_student.html', context)


@login_required
@allowed_users(allowed_roles=['hod'])
def see_detail_view(request, pk):
    stu = Student.objects.get(id=pk)

    context = {'student': stu}
    return render(request, 'HOD/see_detail.html', context)




@login_required
@allowed_users(allowed_roles=['hod'])
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


@login_required
@allowed_users(allowed_roles=['hod'])
def delete_staff_view(request, pk):
    staffs = Staff.objects.get(id=pk)
    if request.method == "POST":
        staffs.user.delete()
        return redirect('manage_staff_view')
    context = {'item': staffs}
    return render(request, 'HOD/delete_staff.html', context)


@login_required
@allowed_users(allowed_roles=['hod'])
def see_detail_staff_view(request, pk):
    sta = Staff.objects.get(id=pk)
    context = {'staff': sta}
    return render(request, 'HOD/see_detail_staff.html', context)


@login_required
@allowed_users(allowed_roles=['hod'])
def result_view(request):
    context = {}
    return render(request, 'HOD/result.html', context)
