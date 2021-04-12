from django.urls import path
from . import views
urlpatterns = [
    path("", views.hod_dashboard, name = 'hod_dashboard'),
    path('dashboard/', views.admin_dashboard, name='admin_dashboard'),
    
    path('add_user/', views.register_user_view, name='register_user'),
    path('add_staff/', views.add_staff, name='add_staff'),
    path('test/', views.test_view, name='test-view'),
    path('charts/', views.charts_view, name='charts_view'),
    path('login/', views.login_view, name='login_view'),
    path('tables/', views.tables_view, name='tables_view'),
    path('manage_student/', views.manage_student_view, name='manage_student_view'),
    path('manage_staff/', views.manage_staff_view, name='manage_staff_view'),
    path('add_student/', views.add_student_view, name='add_student'),
    path('add_staff/', views.add_staff_view, name='add_staff'),
    path('update_student/<str:pk>',
         views.update_student_view, name='update_student'),
    path('update_staff/<str:pk>',
         views.update_staff_view, name='update_staff'),
    path('delete_student/<str:pk>',views.delete_student_view, name='delete_student'),
    path('delete_staff/<str:pk>',views.delete_staff_view, name='delete_staff'),
    path('see_detail/<str:pk>',views.see_detail_view,name='see_detail'),
    path('see_detail_staff/<str:pk>',views.see_detail_staff_view,name='see_detail_staff')

]
