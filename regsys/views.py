from django.shortcuts import render, redirect 
from django.db.models import F, Max, Sum, Avg, Func
from django.db.models.functions import Round
from django.forms import inlineformset_factory
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import *
from .decorators import faculty_only, unauthenticated_user, student_only
from .filters import CourseFilter, SectionFilter, EnrollmentFilter,GradingFilter
from django.contrib.auth.decorators import user_passes_test
from .forms import RegisterForm, UpdateCourseForm, AddSectionForm, AddCourseForm,ChangeGradeForm, StudentForm, StaffForm
from django.db import transaction
from django.contrib.auth.models import User

@login_required(login_url='regsys-login')
@user_passes_test(lambda u: u.is_superuser)
def adminHome(request):
	return render(request, 'regsys/ahome.html')

@login_required(login_url='regsys-login')
@faculty_only
def home(request):
	return render(request, 'regsys/home.html')

@login_required(login_url='regsys-login')
@student_only
def studentHome(request):
	return render(request, 'regsys/shome.html')

@login_required(login_url='regsys-login')
@student_only
def studentProfile(request):
	student = Student.objects.filter(userName=request.user)
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
	register = Registration.objects.filter(stud_id=request.user)
	context = {'register':register}
	return render(request, 'regsys/schedule.html', context)

@login_required(login_url='regsys-login')
@faculty_only
def facultyProfile(request):
  staff = Staff.objects.filter(staffName=request.user)
  context = {'staff':staff}
  return render(request, 'regsys/facultyProfile.html', context)

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

@user_passes_test(lambda u: u.is_superuser)
def addcourse(request):
  up_course = Course.objects.all()
  form = AddCourseForm()

  if request.method == 'POST':
    form = AddCourseForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('regsys-adminHome')
  context = {'form':form,'up_course':up_course}
  return render(request, "regsys/add_course.html",context)

@login_required(login_url='regsys-login')
@student_only
def dropCourse(request, pk):
	sections = Section.objects.all()
	register = Registration.objects.get(id=pk)
	if request.method == "POST":
		register.delete()
		# Section.objects.filter(section_no__in=sections).update(current_enrollment=F('current_enrollment') - 1) 
		return redirect('regsys-studentCatalog')
	context = {'course':register}
	return render(request, 'regsys/drop.html', context)

# WANT TO BE ABLE TO AUTOFILL FORM OF DESIRED SECTION
@login_required(login_url='regsys-login')
@student_only
def studentRegister(request,pk):
	sections = Section.objects.filter(section_no=pk)

	form = RegisterForm()
	if request.method == 'POST':
		form = RegisterForm(request.POST)
		if form.is_valid():
			student = form.save(commit=False)
			student.stud_id = request.user
			student.save()
			Section.objects.filter(section_no__in=sections).update(current_enrollment=F('current_enrollment') + 1) 
			return redirect('regsys-studentCatalog')
	context = {'form':form, 'sections':sections}
	return render(request, 'regsys/registration_form.html', context) 

@login_required(login_url='regsys-login')
@student_only
def studentCatalog(request):
	sections = Section.objects.all()
	myFilter = SectionFilter(request.GET, queryset=sections)
	sections = myFilter.qs
	context = {'sections':sections, 'myFilter':myFilter}
	return render(request, 'regsys/course_catalog.html', context) 

@user_passes_test(lambda u: u.is_superuser)
def update(request,pk):
  up_course = Section.objects.get(section_no=pk)
  form = UpdateCourseForm(instance=up_course)

  if request.method == 'POST':
    form = UpdateCourseForm(request.POST, instance=up_course)
    if form.is_valid():
      form.save()
      return redirect('regsys-updatecourse')
  context = {'form':form}
  return render(request, "regsys/updateSec.html",context)

@user_passes_test(lambda u: u.is_superuser)
def updatecourse(request):
  up_course = Section.objects.all()
  myFilter = SectionFilter(request.GET, queryset=up_course)
  up_course = myFilter.qs	
  context = {'up_course':up_course, 'myFilter':myFilter}
  return render(request, "regsys/update_course.html", context)

@user_passes_test(lambda u: u.is_superuser)
def addsection(request):
  up_course = Section.objects.all()
  form = AddSectionForm()

  if request.method == 'POST':
    form = AddSectionForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('regsys-adminHome')
  context = {'form':form,'up_course':up_course}
  return render(request, "regsys/add_section.html",context)

@user_passes_test(lambda u: u.is_superuser)
def deletesection(request):
	up_course = Section.objects.all()
	myFilter = CourseFilter(request.GET, queryset=up_course)
	up_course = myFilter.qs
	context = {'up_course':up_course, 'myFilter':myFilter}
	if (request.method == 'POST') and (request.POST.get('cno') and request.POST.get('sno')):
		with transaction.atomic():
		  course = Course.objects.get(course_no=request.POST.get('cno'))
		  section = Section.objects.get(section_no=request.POST.get('sno'), course_no=request.POST.get('cno'))
		  if(Section.objects.filter(section_no=request.POST.get('sno'), course_no=request.POST.get('cno')).count() == 0):
		    print(messages.info(request,'No Data Found!'))
		  else:
		    section.delete()
		    return redirect('regsys-deletesection')
		  section2 = Section.objects.get(course_no=request.POST.get('cno'))
		  if(Section.objects.filter(course_no=request.POST.get('cno')).count() == 0):
		    course.delete()
		    return redirect('regsys-adminHome')
	return render(request, "regsys/delete_section.html",context)

@user_passes_test(lambda u: u.is_superuser)
def deletecourse(request):
	del_course = Course.objects.all()
	myFilter = CourseFilter(request.GET, queryset=del_course)
	del_course = myFilter.qs
	context = {'del_course':del_course, 'myFilter':myFilter}
	if (request.method == 'POST') and (request.POST.get('cno')):
		with transaction.atomic():
		  course = Course.objects.get(course_no=request.POST.get('cno'))
		  if(Course.objects.filter(course_no=request.POST.get('cno')).count() == 0):
		    print(messages.info(request,'No Data Found!'))
		  else:
		    course.delete()
		    return redirect('regsys-deletecourse')
	return render(request, "regsys/delete_course.html",context)
      
@user_passes_test(lambda u: u.is_superuser)
def viewstudents(request):
  students = Student.objects.all()
  return render(request, "regsys/student_info.html", {'students':students})

@user_passes_test(lambda u: u.is_superuser)
def viewstaff(request):
  staff = Staff.objects.all()
  return render(request, "regsys/faculty_info.html", {'staff':staff})

@user_passes_test(lambda u: u.is_superuser)
def statistics(request):
  statistics = Section.objects.all()
  context = {'statistics':statistics}
  return render(request, "regsys/statistics.html", context)

@user_passes_test(lambda u: u.is_superuser)
def enrollment(request):
  enrollments = Registration.objects.all()
  myFilter = EnrollmentFilter(request.GET, queryset=enrollments)
  enrollments = myFilter.qs
  context = {'enrollments':enrollments, 'myFilter':myFilter}
  return render(request, "regsys/student_enrollment.html", context)

@login_required(login_url='regsys-login')
@faculty_only
def grading(request,staffName):
	student = Registration.objects.filter(staff_id=staffName)
	myFilter = GradingFilter(request.GET, queryset=student)
	student = myFilter.qs
	context = {'student':student, 'myFilter':myFilter}
	return render(request, "regsys/grading.html", context)

@login_required(login_url='regsys-login')
@faculty_only
def facultyGrading(request,pk):
	student = Registration.objects.filter(id=pk).first()
	form = ChangeGradeForm(instance=student)

	if request.method == 'POST':
		form = ChangeGradeForm(request.POST, instance=student)
		if form.is_valid():
			form.save()
			return redirect('regsys-facultySchedule')
	context = {'form':form,'student':student}
	return render(request, "regsys/facultyRegInfo.html", context)

# COULD POTENTIALLY FILTER FROM REGISTRATION MODEL INSTEAD FOR STAFF
@login_required(login_url='regsys-login')
@faculty_only
def facultySchedule(request):
  staff = Section.objects.filter(staff_id_id=request.user)
  context = {'staff':staff}
  return render(request, 'regsys/facultySchedule.html', context)

@login_required(login_url='regsys-login')
@student_only
def editinfo(request):
	student = Student.objects.filter(userName=request.user).first()
	form = StudentForm()

	if request.method == 'POST':
		form = StudentForm(request.POST, instance=student)
		if form.is_valid():
			form.save()
			return redirect('regsys-studentProfile')
	context = {'form':form, 'student':student}
	return render(request, "regsys/edit_info.html", context)

@login_required(login_url='regsys-login')
@faculty_only
def editFacultyInfo(request):
	staff = Staff.objects.filter(staffName=request.user).first()
	form = StaffForm()

	if request.method == 'POST':
		form = StaffForm(request.POST, instance=staff)
		if form.is_valid():
			form.save()
			return redirect('regsys-facultyProfile')
	context = {'form':form, 'staff':staff}
	return render(request, "regsys/edit_finfo.html", context)

@login_required(login_url='regsys-login')
@student_only
def transcript(request):
  transcripts = Registration.objects.all().values(
	  'course_no', 'course_no__course_name',
    'year', 'semester', 'course_no__credit', 'grade').filter(stud_id=request.user).order_by('year','semester')
  summary = Registration.objects.values('stud_id').filter(stud_id=request.user).annotate(cred = Sum('course_no__credit'), average = Avg('grade'))  
  context = {'transcripts':transcripts, 'summary':summary}
  return render(request, "regsys/student_transcript.html", context)