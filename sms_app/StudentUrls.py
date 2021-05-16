from django.urls import path
from . import Student_views

urlpatterns = [
    path("", Student_views.dashboard_view, name='dashboard'),
    path("attendence", Student_views.attendence_view, name='attendence'),
    path("result", Student_views.result_view, name='result'),
    path("leave", Student_views.leave_view, name='leave'),
    path("feedback", Student_views.feedback_view, name='feedback'),
]

     