from django.http import HttpResponse
from django.shortcuts import redirect
	
def unauthenticated_user(view_func):
	def wrapper_func(request, *args, **kwargs):
		group = None
		if request.user.groups.exists():
			group = request.user.groups.all()[0].name
		if request.user.is_authenticated and group=='Student':
			return redirect('regsys-studentHome')
		elif request.user.is_authenticated and group=='Faculty':
			return redirect('regsys-home')
		else:
			return view_func(request, *args, **kwargs)
	return wrapper_func

def faculty_only(view_func):
	def wrapper_function(request, *args, **kwargs):
		group = None
		if request.user.groups.exists():
			group = request.user.groups.all()[0].name
		if group == 'Student':
			return redirect('regsys-studentHome')
		if group == 'Faculty':
			return view_func(request, *args, **kwargs)
	return wrapper_function

def student_only(view_func):
	def wrapper_function(request, *args, **kwargs):
		group = None
		if request.user.groups.exists():
			group = request.user.groups.all()[0].name
		if group == 'Faculty':
			return redirect('regsys-home')
		if group == 'Student':
			return view_func(request, *args, **kwargs)
	return wrapper_function