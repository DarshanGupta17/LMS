"""
URL configuration for SMS project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .import views,Hod_views,Staff_views,Student_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('base/', views.BASE, name='base'),

    # Login Path
    path('', views.LOGIN, name='Login'),
    path('doLogin', views.doLogin, name='doLogin'),
    path('doLogout', views.doLogout, name='doLogout'),

    # Profile Update Path
    path('profile', views.profile, name='profile'),
    path('profile/update', views.PROFILE_UPDATE, name="profile_update"),

    # HOD Pannel paths
    path('Hod/home', Hod_views.home, name='hod_home'),
    path('Hod/Student/Add', Hod_views.Add_Student, name="Add_Student"),
    path('Hod/Student/View', Hod_views.VIEW_STUDENT, name="View_Student"),
    path('Hod/Student/Edit/<str:id>', Hod_views.EDIT_STUDENT, name="Edit_Student"),
    path('Hod/Student/Update', Hod_views.UPDATE_STUDENT, name="Update_Student"),
    path('Hod/Student/Delete/<str:admin>', Hod_views.DELETE_STUDENT, name="Delete_Student"),

    path('Hod/Course/Add', Hod_views.ADD_COURSE, name="Add_Course"),
    path('Hod/Course/View', Hod_views.VIEW_COURSE, name="View_Course"),
    path('Hod/Course/Edit/<str:id>', Hod_views.EDIT_COURSE, name="Edit_Course"),
    path('Hod/Course/Update', Hod_views.UPDATE_COURSE, name="Update_Course"),
    path('Hod/Course/Delete/<str:id>', Hod_views.DELETE_COURSE, name="Delete_Course"),

    path('Hod/Staff/Add', Hod_views.ADD_STAFF, name="Add_Staff"),
    path('Hod/Staff/View', Hod_views.VIEW_STAFF, name="View_Staff"),
    path('Hod/Staff/Edit/<str:id>', Hod_views.EDIT_STAFF, name="Edit_Staff"),
    path('Hod/Staff/Update', Hod_views.UPDATE_STAFF, name="Update_Staff"),
    path('Hod/Staff/Delete/<str:admin>', Hod_views.DELETE_STAFF, name="Delete_Staff"),

    path('Hod/Subject/Add', Hod_views.ADD_SUBJECT, name="Add_Subject"),
    path('Hod/Subject/View', Hod_views.VIEW_SUBJECT, name="View_Subject"),
    path('Hod/Subject/Edit/<str:id>', Hod_views.EDIT_SUBJECT, name="Edit_Subject"),
    path('Hod/Subject/Update', Hod_views.UPDATE_SUBJECT, name="Update_Subject"),
    path('Hod/Subject/Delete/<str:id>', Hod_views.DELETE_SUBJECT, name="Delete_Subject"),

    path('Hod/Session/Add', Hod_views.ADD_SESSION, name="Add_Session"),
    path('Hod/Session/View', Hod_views.VIEW_SESSION, name="View_Session"),
    path('Hod/Session/Edit/<str:id>', Hod_views.EDIT_SESSION, name="Edit_Session"),
    path('Hod/Session/Update', Hod_views.UPDATE_SESSION, name="Update_Session"),
    path('Hod/Session/Delete/<str:id>', Hod_views.DELETE_SESSION, name="Delete_Session"),

    path('Hod/Staff/Send_Notification', Hod_views.STAFF_SEND_NOTI, name="Staff_Send_Noti"),
    path('Hod/Staff/Save_Notification', Hod_views.SAVE_STAFF_NOTI, name="Save_Staff_Noti"),

    path('Hod/Student/Send_Notification', Hod_views.STUD_SEND_NOTI, name="Student_Send_Noti"),
    path('Hod/Student/Save_Notification', Hod_views.SAVE_STUD_NOTI, name="Save_Student_Noti"),

    path('Hod/Staff/Leave_View', Hod_views.STAFF_LEAVE_VIEW, name="Staff_Leave_View"),
    path('Hod/Staff/Approve_Leave/<str:id>', Hod_views.STAFF_APPROVE_LEAVE, name="Staff_Approve_Leave"),
    path('Hod/Staff/Disapprove_Leave/<str:id>', Hod_views.STAFF_DISAPPROVE_LEAVE, name="Staff_Disapprove_Leave"),

    path('Hod/Student/Leave_View', Hod_views.STUD_LEAVE_VIEW, name="Stud_Leave_View"),
    path('Hod/Student/Approve_Leave/<str:id>', Hod_views.STUD_APPROVE_LEAVE, name="Stud_Approve_Leave"),
    path('Hod/Student/Disapprove_Leave/<str:id>', Hod_views.STUD_DISAPPROVE_LEAVE, name="Stud_Disapprove_Leave"),

    path('Hod/Staff/Feedback', Hod_views.STAFF_FEEDBACK_REPLY, name="Staff_Feedback_Reply"),
    path('Hod/Staff/Feedback/Save', Hod_views.STAFF_FEEDBACK_REPLY_SAVE, name="Staff_Feedback_Reply_Save"),

    path('Hod/Student/Feedback', Hod_views.STUD_FEEDBACK_REPLY, name="Stud_Feedback_Reply"),
    path('Hod/Student/Feedback/Save', Hod_views.STUD_FEEDBACK_REPLY_SAVE, name="Stud_Feedback_Reply_Save"),

    path('Hod/View_Attendance', Hod_views.HOD_VIEW_ATTENDANCE,name='hod_view_attendance'),

    path('Hod/Add_Activity',Hod_views.ADD_STUDENT_ACTIVITY,name='add_student_activity'),
    path('Hod/Save_Activity',Hod_views.SAVE_STUDENT_ACTIVITY,name='save_student_activity'),

    # Staff Pannel Path
    path('Staff/Home', Staff_views.HOME, name="staff_home"),

    path('Staff/Notifications', Staff_views.NOTIFICATIONS, name="Notifications"),
    path('Staff/Mark_as_Done/<str:status>', Staff_views.NOTI_MARK_AS_DONE, name="Mark_As_Done"),

    path('Staff/Apply_Leave', Staff_views.APPLY_LEAVE, name="Apply_Leave"),
    path('Staff/Apply_Leave_Save', Staff_views.APPLY_LEAVE_SAVE, name="Apply_Leave_Save"),

    path('Staff/Feedback', Staff_views.STAFF_FEEDBACK, name="Staff_Feedback"),
    path('Staff/Feedback/Save', Staff_views.STAFF_FEEDBACK_SAVE, name="Staff_Feedback_Save"),
    path('staff/Take_Attendance' , Staff_views.STAFF_TAKE_ATTENDANCE,name="staff_take_attendance"),
    path('staff/Save_Attendance',Staff_views.STAFF_SAVE_ATTENDANCE,name='staff_save_attendance'),
    path('staff/View_Attendance',Staff_views.VIEW_ATTENDANCE,name='staff_view_attendance'),
    path('staff/Add_Result',Staff_views.STAFF_ADD_RESULT,name='staff_add_result'),
    path('staff/Save_Result',Staff_views.STAFF_SAVE_RESULT,name='staff_save_result'),

    # Student Pannel Path
    path('Student/Home', Student_views.HOME, name="Student_Home"),

    path('Student/Notifications', Student_views.STUD_NOTIFICATION, name="Stud_Notification"),
    path('Student/Mark_as_Done/<str:status>', Student_views.NOTI_MARK_AS_DONE, name="Stud_Mark_As_Done"),

    path('Student/Feedback', Student_views.STUD_FEEDBACK, name="Stud_Feedback"),
    path('Student/Feedback/Save', Student_views.STUD_FEEDBACK_SAVE, name="Stud_Feedback_Save"),

    path('Student/Apply_Leave', Student_views.APPLY_FOR_LEAVE, name="Stud_Apply_Leave"),
    path('Student/Apply_Leave_Save', Student_views.STUD_APPLY_LEAVE_SAVE, name="Stud_Apply_Leave_Save"),
    path('student/View_Attendance',Student_views.STUD_VIEW_ATTENDANCE,name='student_view_attendance'),
    path('student/View_Result',Student_views.VIEW_RESULT,name='student_view_result')
   
] + static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
