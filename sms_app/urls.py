from django.urls import path
from .views import admin_dashboard, add_staff, register_user_view, test_view
urlpatterns = [
    path('', admin_dashboard, name='admin_dashboard'),
    path('add_user/', register_user_view, name='register_user'),
    path('add_staff/', add_staff, name='add_staff'),
    path('test/', test_view, name='test-view')
]
