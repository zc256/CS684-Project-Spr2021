from django.forms import ModelForm
from .models import Registration, Section, Course, Student, Staff
from django import forms

class RegisterForm(ModelForm):
	class Meta:
		model = Registration
		fields = '__all__'
		exclude = ['stud_id','grade']

class UpdateCourseForm(ModelForm):
	class Meta:
		model = Section
		fields = '__all__'

class AddSectionForm(ModelForm):
	class Meta:
		model = Section
		fields = '__all__'

class AddCourseForm(ModelForm):
	class Meta:
		model = Course
		fields = '__all__'

class ChangeGradeForm(ModelForm):
	class Meta:
		model = Registration
		fields = ('stud_id','grade')

class StudentForm(ModelForm):
	class Meta:
		model = Student
		fields = '__all__'
		exclude = ['student_id', 'userName','ssn', 'name','dep_code', 'email', 'gender']

class StaffForm(ModelForm):
	class Meta:
		model = Staff
		fields = '__all__'
		exclude = ['staffName','ssn','email','salary','rank','name']