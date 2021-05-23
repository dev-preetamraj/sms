from django.urls import path
from . import Staff_views

urlpatterns = [
    path("", Staff_views.staff_dashboard, name='staff_dashboard'),
    path('staff_take_attendance/', Staff_views.staff_take_attendance, name="staff_take_attendance"),
    path('get_students/', Staff_views.get_students, name="get_students"),
    path('save_attendance_data/', Staff_views.save_attendance_data, name="save_attendance_data"),
    path("view_attendance/", Staff_views.view_attendance, name='staffView_attendance'),
    path('staff_get_attendance_dates/',Staff_views.staff_get_attendance_dates,name='staff_get_attendance_dates'),
    path('staff_get_attendance_student/',Staff_views.staff_get_attendance_student,name='staff_get_attendance_student'),
    path("add_result/", Staff_views.add_result, name='add_result'),
    path("leave/", Staff_views.leave, name='leaveStaff'),
    path('staff_leave_save', Staff_views.staff_leave_save,name='staff_leave_save'),
    path("feedback/", Staff_views.feedback, name='feedbackStaff'),
    path("save_staff_feedback/",Staff_views.save_staff_feedback,name='save_staff_feedback')
]