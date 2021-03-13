from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Department(models.Model):
	dep_name = models.CharField(max_length=30, default='None')
	annual_budget = models.FloatField()
	dep_chair = models.CharField(max_length=100, default='None')

	def __str__(self):
		return self.dep_name

class Course(models.Model):
	course_no = models.CharField(primary_key=True, max_length=10)
	course_name = models.CharField(max_length=30, default='None')
	credit = models.IntegerField()
	dep_code = models.ForeignKey(Department, on_delete=models.CASCADE)

	def __str__(self):
		return self.course_name

class Staff(models.Model):
	ssn = models.CharField(max_length=10, default="0000000000")
	name = models.CharField(max_length=100, default="None")	
	address = models.CharField(max_length=80, default='None')
	email = models.EmailField(max_length=254)
	mob_no = models.CharField(max_length=20, default='None')
	salary = models.FloatField()
	rank = models.CharField(max_length=20, default='None')

	def __str__(self):
		return self.name

class Building(models.Model):
	building_code = models.CharField(primary_key=True, max_length=20)
	building_name = models.CharField(max_length=50, default='None')
	location = models.CharField(max_length=50, default='None')

	def __str__(self):
		return self.building_name
	
class Section(models.Model):
	section_no = models.CharField(primary_key=True, max_length=10)
	section_name = models.CharField(max_length=10, default='None')
	year = models.IntegerField()
	semester = models.CharField(max_length=15, default='None')
	weekday = models.CharField(max_length=10, default='None')
	start = models.CharField(max_length=10, default='None')
	end = models.CharField(max_length=10, default='None')
	current_enrollment = models.IntegerField()
	max_enrollment = models.IntegerField()
	course_no = models.ForeignKey(Course, on_delete=models.CASCADE)
	staff_id = models.ForeignKey(Staff, on_delete=models.CASCADE)
	building_code = models.ForeignKey(Building, on_delete=models.CASCADE)

	def __str__(self):
		return self.section_name

class Student(models.Model):
	GENDER = [
		('M', 'Male'),
		('F', 'Female'),
		('O', 'Other'),
	]
	ssn = models.CharField(max_length=10, default="0000000000")
	name = models.CharField(max_length=100, default="None")
	gender = models.CharField(max_length=10, choices=GENDER)
	address = models.CharField(max_length=80, default='None')
	mob_no = models.CharField(max_length=10, default='None')
	email = models.EmailField(max_length=254)
	userName = models.ForeignKey(User, on_delete=models.CASCADE)
	dep_code = models.ForeignKey(Department, on_delete=models.CASCADE)
	gpa = models.FloatField()

	def __str__(self):
		return self.name

class Admin(models.Model):
	f_name = models.CharField(max_length=50, default='None')
	l_name = models.CharField(max_length=50, default='None')
	mob_no = models.CharField(max_length=20, default='None')
	email = models.EmailField(max_length=254)
	student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
	staff_id = models.ForeignKey(Staff, on_delete=models.CASCADE)

	def __str__(self):
		return self.f_name + ' ' + self.l_name

class Registration(models.Model):
	semester = models.CharField(max_length=15, default='None')
	year = models.IntegerField()
	student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
	course_no = models.ForeignKey(Course, on_delete=models.CASCADE)
	section_no = models.ForeignKey(Section, on_delete=models.CASCADE)

	# def __str__(self):
	# 	return self.student_id

class Student_Enrollment(models.Model):
	# course_no = models.CharField(max_length=10, default='None')
	semester = models.CharField(max_length=15, default='None')
	year = models.IntegerField()
	# section_no = models.CharField(max_length=5, default='None')
	grade = models.CharField(max_length=3, default='None')
	student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
	course_no = models.ForeignKey(Course, on_delete=models.CASCADE)
	section_no = models.ForeignKey(Section, on_delete=models.CASCADE)


class Room(models.Model):
	room_no = models.CharField(max_length=20, default='None')
	capacity = models.IntegerField()
	audio_visual = models.CharField(max_length=20, default='None')
	building_code = models.ForeignKey(Building, on_delete=models.CASCADE)

	def __str__(self):
		return self.room_no

class faculty_department(models.Model):
	staff_id = models.ForeignKey(Staff, on_delete=models.CASCADE)
	dep_code = models.ForeignKey(Department, on_delete=models.CASCADE)