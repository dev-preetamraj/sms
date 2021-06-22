from django.urls import path
from . import HODviews

urlpatterns = [
    path("", HODviews.hod_dashboard, name='hod_dashboard'),

    path('dashboard/', HODviews.admin_dashboard, name='admin_dashboard'),

    path('add_user/', HODviews.register_user_view, name='register_user'),
    #     path('add_staff/', HODviews.add_staff, name='add_staff'),
    path('test/', HODviews.test_view, name='test-view'),
    path('result/', HODviews.result_view, name='result-view'),
    path('charts/', HODviews.charts_view, name='charts_view'),
    path('login/', HODviews.login_view, name='login_view'),
    path('tables/', HODviews.tables_view, name='tables_view'),
    path('manage_student/', HODviews.manage_student_view, name='manage_student_view'),
    path('manage_staff/', HODviews.manage_staff_view, name='manage_staff_view'),
    path('manage_courses/', HODviews.manage_courses_view, name='manage_courses_view'),
    path('add_course/', HODviews.add_course_view, name='add_course_view'),
    path('manage_subjects/', HODviews.manage_subjects_view,
         name='manage_subjects_view'),
    path('manage_sessions/', HODviews.manage_sessions_view,
         name='manage_sessions_view'),
    path('view_attendance/', HODviews.view_attendance, name='view_attendance'),
    path('staff_feedback/', HODviews.staff_feedback_view, name='staff_feedback_view'),
    path('staff_feedback_message_reply/',HODviews.staff_feedback_message_reply,name='staff_feedback_message_reply'),
    path('student_feedback_message_reply/',HODviews.student_feedback_message_reply,name='student_feedback_message_reply'),
    path('students_feedback/', HODviews.students_feedback_view,
         name='students_feedback_view'),
    path('staff_leave/', HODviews.staff_leave_view, name='staff_leave_view'),
    path('staff_leave_approve/<str:leave_id>/',HODviews.staff_leave_approve,name='staff_leave_approve'),
    path('staff_leave_reject/<str:leave_id>/',HODviews.staff_leave_reject,name='staff_leave_reject'),
    path('student_leave/', HODviews.student_leave_view, name='student_leave_view'),
    path('student_leave_approve/<str:leave_id>/',HODviews.student_leave_approve,name='student_leave_approve'),
    path('student_leave_reject/<str:leave_id>/',HODviews.student_leave_reject,name='student_leave_reject'),
     path('add_subjects/', HODviews.add_subjects_view, name='add_subjects'),
     path('add_session/', HODviews.add_session_view, name='add_session'),
    path('update_student/<str:pk>',
         HODviews.update_student_view, name='update_student'),
    path('update_staff/<str:pk>',
         HODviews.update_staff_view, name='update_staff'),
    path('delete_student/<str:pk>',
         HODviews.delete_student_view, name='delete_student'),
    path('delete_staff/<str:pk>', HODviews.delete_staff_view, name='delete_staff'),
    path('delete_session/<str:pk>', HODviews.delete_session_view, name='delete_session'),
    path('update_session/<str:pk>',
         HODviews.update_session_view, name='update_session'),
    path('see_detail/<str:pk>', HODviews.see_detail_view, name='see_detail'),
    path('see_detail_staff/<str:pk>',
         HODviews.see_detail_staff_view, name='see_detail_staff'),

         #------------------------url for students-----------------------------------

         #------------------------url for staffs-------------------------------------

]
