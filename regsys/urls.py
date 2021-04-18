from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='regsys-home'),
    path('catalog/', views.studentCatalog, name='regsys-studentCatalog'),
    path('facprof/', views.facultyProfile, name='regsys-facultyProfile'),  
    path('register/<str:pk>/', views.studentRegister, name='regsys-studentRegister'),
    path('schedule/', views.studentSchedule, name='regsys-studentSchedule'),
    path('facultySchedule/', views.facultySchedule, name='regsys-facultySchedule'),
    path('grading/<int:pk>/', views.grading, name='regsys-grading'),    
	path('changeGrade/<str:pk>', views.facultyGrading, name='regsys-facGrading'),
	path('shome/', views.studentHome, name='regsys-studentHome'),       
    path('studentprof/', views.studentProfile, name='regsys-studentProfile'),
    path('drop/<str:pk>/', views.dropCourse, name='regsys-drop'),
    path('login/', views.loginPage, name='regsys-login'),
    path('logout/', views.logoutUser, name='regsys-logout'),
    path('ahome/', views.adminHome, name='regsys-adminHome'), #admin
    path("addcourse/", views.addcourse, name="regsys-addcourse"), #admin
    path("updatecourse/", views.updatecourse, name="regsys-updatecourse"), #admin
    path("update/<str:pk>/", views.update, name="regsys-update"), #admin
    path("addsection/", views.addsection, name='regsys-addsection'), #admin
    path("deletesection/", views.deletesection, name="regsys-deletesection"), #admin
    path("deletecourse/", views.deletecourse, name="regsys-deletecourse"), #admin
    path("students/", views.viewstudents, name="regsys-viewstudents"), #admin
    path("staff/", views.viewstaff, name="regsys-viewstaff"), #admin
    path("statistics/", views.statistics, name="regsys-viewstats"), #admin
    path("enrollment/", views.enrollment, name="regsys-enrollment"),
    path("editinfo/", views.editinfo, name="regsys-editinfo"),
    path("editFacultyInfo/", views.editFacultyInfo, name="regsys-editFacultyInfo"),
    path("transcript/", views.transcript, name="regsys-transcript")
]