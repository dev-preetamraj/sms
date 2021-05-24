from django.contrib import messages
from django.shortcuts import render, redirect
from .decorators import allowed_users, unauthenticated_user
from django.contrib.auth.models import User, Group
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.detail import DetailView
from django.contrib.auth.decorators import login_required
from accounts.decorators import allowed_users
from .models import Attendance, SessionYear, Staff_Leave, Staffs_FeedBack, Staff, Student, StudentAttendance, Subject
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, request
import datetime
import json

@login_required
@allowed_users(allowed_roles=['staff'])
def staff_dashboard(req):
    context = {}
    return render(req, 'Staff/dashboard.html', context)

@login_required
@allowed_users(allowed_roles=['staff'])
def staff_take_attendance(request):
    staff_obj = Staff.objects.get(user=request.user.id)
    subjects = Subject.objects.filter(taught_by=staff_obj)
    session_years = SessionYear.objects.all()
    context = {
        "subjects": subjects,
        "session_years": session_years
    }
    return render(request, 'Staff/take_attendance.html', context)

@csrf_exempt
def get_students(request):
    # Getting Values from Ajax POST 'Fetch Student'
    subject_id = request.POST.get("subject")
    session_year = request.POST.get("session_year")

    # Students enroll to Course, Course has Subjects
    # Getting all data from subject model based on subject_id
    subject_model = Subject.objects.get(id=subject_id)

    session_model = SessionYear.objects.get(id=session_year)

    students = Student.objects.filter(courses_taken=subject_model.under_course, session_under=session_model)

    # Only Passing Student Id and Student Name Only
    list_data = []

    for student in students:
        data_small={"id":student.user.id, "name":student.user.first_name+" "+student.user.last_name}
        list_data.append(data_small)

    return JsonResponse(json.dumps(list_data), content_type="application/json", safe=False)


@csrf_exempt
def save_attendance_data(request):
    # Get Values from Staf Take Attendance form via AJAX (JavaScript)
    # Use getlist to access HTML Array/List Input Data
    student_ids = request.POST.get("student_ids")
    subject_id = request.POST.get("subject_id")
    attendance_date = request.POST.get("attendance_date")
    session_year_id = request.POST.get("session_year_id")

    subject_model = Subject.objects.get(id=subject_id)
    session_year_model = SessionYear.objects.get(id=session_year_id)

    json_student = json.loads(student_ids)
    # print(dict_student[0]['id'])

    # print(student_ids)
    try:
        # First Attendance Data is Saved on Attendance Model
        attendance = Attendance(subject_id=subject_model, attendance_date=attendance_date, session_year_id=session_year_model)
        attendance.save()

        for stud in json_student:
            # Attendance of Individual Student saved on AttendanceReport Model
            student = Student.objects.get(user=stud['id'])
            attendance_report = StudentAttendance(student_id=student, attendance_id=attendance, attendance_type=stud['status'])
            attendance_report.save()
        return HttpResponse("OK")
    except:
        return HttpResponse("Error")

@login_required
@allowed_users(allowed_roles=['staff'])
def view_attendance(request):
    staff_obj = Staff.objects.get(user = request.user.id)
    subjects_taught = Subject.objects.filter(taught_by=staff_obj)
    sessions = SessionYear.objects.all()
    context = {
        'subjects_taught': subjects_taught,
        'sessions': sessions
    }
    return render(request, 'Staff/view_attendance.html', context)

@csrf_exempt
def staff_get_attendance_dates(request):
    # Getting Values from Ajax POST 'Fetch Student'
    subject_id = request.POST.get("subject")
    session_year = request.POST.get("session_year_id")

    # Students enroll to Course, Course has Subjects
    # Getting all data from subject model based on subject_id
    subject_model = Subject.objects.get(id=subject_id)

    session_model = SessionYear.objects.get(id=session_year)

    # students = Students.objects.filter(course_id=subject_model.course_id, session_year_id=session_model)
    attendance = Attendance.objects.filter(subject_id=subject_model, session_year_id=session_model)

    # Only Passing Student Id and Student Name Only
    list_data = []

    for attendance_single in attendance:
        data_small={"id":attendance_single.id, "attendance_date":str(attendance_single.attendance_date), "session_year_id":attendance_single.session_year_id.id}
        list_data.append(data_small)

    return JsonResponse(json.dumps(list_data), content_type="application/json", safe=False)

@csrf_exempt
def staff_get_attendance_student(request):
    # Getting Values from Ajax POST 'Fetch Student'
    attendance_date = request.POST.get('attendance_date')
    attendance = Attendance.objects.get(id=attendance_date)

    attendance_data = StudentAttendance.objects.filter(attendance_id=attendance)
    # Only Passing Student Id and Student Name Only
    list_data = []

    for student in attendance_data:
        data_small={"id":student.student_id.user.id, "name":student.student_id.user.first_name+" "+student.student_id.user.last_name, "status":student.attendance_type}
        list_data.append(data_small)

    return JsonResponse(json.dumps(list_data), content_type="application/json", safe=False)



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

