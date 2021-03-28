from django.forms import ModelForm
from .models import Registration, Section, Course
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