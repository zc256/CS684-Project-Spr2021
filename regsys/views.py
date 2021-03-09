from django.shortcuts import render, redirect 
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import *
from .decorators import faculty_only, unauthenticated_user, student_only
from .filters import CourseFilter

@login_required(login_url='regsys-login')
@faculty_only
def home(request):
	return render(request, 'regsys/home.html')

def about(request):
	return render(request, 'regsys/about.html')

def contact(request):
	return render(request, 'regsys/contact.html')

@login_required(login_url='regsys-login')
@student_only
def studentHome(request):
	return render(request, 'regsys/shome.html')

@login_required(login_url='regsys-login')
@student_only
def studentProfile(request):
	return render(request, 'regsys/studentProfile.html')

@login_required(login_url='regsys-login')
@student_only
def studentRegister(request):
	return render(request, 'regsys/registration_form.html') 

@login_required(login_url='regsys-login')
@student_only
def studentCatalog(request):
	courses = Course.objects.all()

	myFilter = CourseFilter(request.GET, queryset=courses)
	courses = myFilter.qs
	context = {'courses':courses, 'myFilter':myFilter}
	return render(request, 'regsys/course_catalog.html', context) 

@login_required(login_url='regsys-login')
@faculty_only
def facultyProfile(request):
	return render(request, 'regsys/facultyProfile.html')

@unauthenticated_user
def loginPage(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password =request.POST.get('password')

		user = authenticate(request, username=username, password=password)

		if user is not None:
			login(request, user)
			return redirect('regsys-home')
		else:
			messages.info(request, 'Username OR password is incorrect')

	context = {}
	return render(request, 'regsys/login.html', context)

def logoutUser(request):
	logout(request)
	return redirect('regsys-login')