from django.urls import path
from . import Student_views

urlpatterns = [
    path("", Student_views.student_home_view, name='student_home'),
    path("student_view_attendence", Student_views.student_view_attendence_view, name='student_view_attendence'),
    path("student_result", Student_views.student_result_view, name='student_result'),
    path("student_apply_leave/<str:pk>", Student_views.student_apply_leave_view, name='student_apply_leave'),
    path("student_send_feedback", Student_views.student_send_feedback_view, name='student_send_feedback'),
]

     