from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Department(models.Model):
	dep_code = models.CharField(max_length=20)
	department = models.CharField(max_length=20, default='None')
	annual_budget = models.CharField(max_length=7, default=10000)
	dep_chair = models.CharField(max_length=15, default='None')

	def __str__(self):
		return self.dep_code

class Course(models.Model):
	dep_name = models.ForeignKey(Department, on_delete=models.CASCADE)
	course_num = models.CharField(max_length=10, default='None')
	course_name = models.CharField(max_length=20, default='None')
	description = models.TextField(max_length=200, default='None')
	credits = models.IntegerField(default=3)

	def __str__(self):
		return self.course_num


'''
class Admin(models.Model):
	admin_ID =
	f_name = 
	l_name = 
	mob_no = 
	email =
	student_ID =
	staff_ID = 

class Student(models.Model):
	student_ID =
	f_name =
	l_name = 
	mob_no = 
	email = 
	address =
	ssn = 
	dep_code = 
	dob = 
	gender = 

class Faculty(models.Model):
	staff_ID = 
	f_name = 
	l_name =
	address = 
	mob_no = 
	email =
	salary = 
	rank = 
	course_load = 
	work_hr = 

class Registration(models.Model):
	student_ID =
	course_no =
	section_no =
	semester = 
	year = 

class Student_Enrollment(models.Model):
	student_ID =
	semester = 
	year = 
	course_name = 
	credits = 
	ta_hr_req = 
	dep_code =

'''