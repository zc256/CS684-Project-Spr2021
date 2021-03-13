from django.shortcuts import render, redirect 
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import *
from .decorators import faculty_only, unauthenticated_user, student_only
from .filters import CourseFilter, SectionFilter
from django.contrib.auth.decorators import user_passes_test
from .forms import RegisterForm

@login_required(login_url='regsys-login')
@user_passes_test(lambda u: u.is_superuser)
def adminHome(request):
	return render(request, 'regsys/ahome.html')

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
def studentRegister(request):
	sections = Section.objects.all()
	form = RegisterForm()

	if request.method == 'POST':
		form = RegisterForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('regsys-studentCatalog')
			
	context = {'form':form, 'sections':sections}
	return render(request, 'regsys/registration_form.html', context) 

@login_required(login_url='regsys-login')
@student_only
def studentProfile(request):
	student = Student.objects.all()

	context = {'student':student}
	return render(request, 'regsys/studentProfile.html', context)

@login_required(login_url='regsys-login')
@student_only
def studentCatalog(request):
	sections = Section.objects.all()

	myFilter = SectionFilter(request.GET, queryset=sections)
	sections = myFilter.qs
	context = {'sections':sections, 'myFilter':myFilter}
	return render(request, 'regsys/course_catalog.html', context) 

@login_required(login_url='regsys-login')
@student_only
def studentSchedule(request):
	register = Registration.objects.all()

	context = {'register':register}
	return render(request, 'regsys/schedule.html', context)

@login_required(login_url='regsys-login')
@student_only
def dropCourse(request, pk):
	register = Registration.objects.get(id=pk)
	if request.method == "POST":
		register.delete()
		return redirect('regsys-studentCatalog')
	context = {'course':register}
	return render(request, 'regsys/drop.html', context)

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

		if user.is_superuser:
			login(request, user)
			return redirect('regsys-adminHome')
		elif user is not None:
			login(request, user)
			return redirect('regsys-home')
		else:
			messages.info(request, 'Username OR password is incorrect')

	context = {}
	return render(request, 'regsys/login.html', context)

def logoutUser(request):
	logout(request)
	return redirect('regsys-login')