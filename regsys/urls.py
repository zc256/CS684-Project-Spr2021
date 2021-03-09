from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='regsys-home'),
    path('about/', views.about, name='regsys-about'),
    path('contact/', views.contact, name='regsys-contact'),
    path('catalog/', views.studentCatalog, name='regsys-studentCatalog'),
    path('facprof/', views.facultyProfile, name='regsys-facultyProfile'),  
    path('register/', views.studentRegister, name='regsys-studentRegister'),
    path('shome/', views.studentHome, name='regsys-studentHome'),       
    path('studentprof/', views.studentProfile, name='regsys-studentProfile'),
    path('login/', views.loginPage, name='regsys-login'),
    path('logout/', views.logoutUser, name='regsys-logout'),
]