from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='regsys-home'),
    path('ahome/', views.adminHome, name='regsys-adminHome'),
    path('about/', views.about, name='regsys-about'),
    path('contact/', views.contact, name='regsys-contact'),
    path('catalog/', views.studentCatalog, name='regsys-studentCatalog'),
    path('drop/<str:pk>/', views.dropCourse, name='regsys-drop'),
    path('facprof/', views.facultyProfile, name='regsys-facultyProfile'),  
    path('register/', views.studentRegister, name='regsys-studentRegister'),
    path('schedule/', views.studentSchedule, name='regsys-studentSchedule'),
    path('shome/', views.studentHome, name='regsys-studentHome'),       
    path('studentprof/', views.studentProfile, name='regsys-studentProfile'),
    path('login/', views.loginPage, name='regsys-login'),
    path('logout/', views.logoutUser, name='regsys-logout'),
]