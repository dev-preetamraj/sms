from django.urls import path
from .views import admin_dashboard, add_staff
urlpatterns = [
    path('', admin_dashboard, name='admin_dashboard'),
    path('add_staff/', add_staff, name='add_staff')
]
