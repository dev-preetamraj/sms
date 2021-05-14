from django.urls import path
from . import Staff_views

urlpatterns = [
    path("", Staff_views.staff_dashboard, name='staff_dashboard'),
]