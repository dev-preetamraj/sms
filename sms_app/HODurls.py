from django.urls import path
from . import views
urlpatterns = [
    path('', views.admin_dashboard, name='admin_dashboard'),
    path('add_user/', views.register_user_view, name='register_user'),
    path('add_staff/', views.add_staff, name='add_staff'),
    path('test/', views.test_view, name='test-view'),
    path('charts/',views.charts_view, name='charts_view'),
    path('tables/',views.tables_view, name='tables_view'),
    path('login/',views.login_view, name='login_view')
]
