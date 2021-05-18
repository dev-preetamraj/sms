from django.urls import path
from . import Staff_views

urlpatterns = [
    path("", Staff_views.staff_dashboard, name='staff_dashboard'),
    path("attendance/", Staff_views.take_attendance, name='take_attendance'),
    path("view_attendance/", Staff_views.view_attendance, name='staffView_attendance'),
    path("add_result/", Staff_views.add_result, name='add_result'),
    path("leave/", Staff_views.leave, name='leaveStaff'),
    path('staff_leave_save', Staff_views.staff_leave_save,name='staff_leave_save'),
    path("feedback/", Staff_views.feedback, name='feedbackStaff'),
    path("save_staff_feedback/",Staff_views.save_staff_feedback,name='save_staff_feedback')
]