from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator, RegexValidator
from phone_field import PhoneField

class Department(models.Model):
	dep_code = models.CharField(primary_key=True, max_length=20, default='None')
	dep_name = models.CharField(max_length=30, default='None')
	annual_budget = models.FloatField()
	dep_chair = models.CharField(max_length=100, default='None')

	def __str__(self):
		return self.dep_name

class Course(models.Model):
	course_no = models.CharField(primary_key=True, max_length=10)
	course_name = models.CharField(max_length=30, default='None')
	credit = models.IntegerField(default=3)
	dep_code = models.ForeignKey(Department, on_delete=models.CASCADE)

	def __str__(self):
		return self.course_no

class Staff(models.Model):
	staffName = models.ForeignKey(User, on_delete=models.CASCADE)
	ssn = models.CharField(max_length=10, default="0000000000")
	name = models.CharField(max_length=100, default="None")	
	address = models.CharField(max_length=80, default='None')
	email = models.EmailField(max_length=254)
	phone_number = PhoneField(blank=True,E164_only=False)
	salary = models.FloatField()
	rank = models.CharField(max_length=20, default='None')

	def __str__(self):
		return str(self.staffName)

class Building(models.Model):
	building_code = models.CharField(primary_key=True, max_length=20)
	building_name = models.CharField(max_length=50, default='None')
	location = models.CharField(max_length=50, default='None')

	def __str__(self):
		return self.building_name
	
class Section(models.Model):
	SEMESTER = [
		('Fall', 'Fall'),
		('Spring', 'Spring'),
	]

	WEEKDAY = [
		('Monday','Monday'),
		('Tuesday', 'Tuesday'),
		('Wednesday','Wednesday'),
		('Thursday', 'Thursday'),
		('Friday','Friday'),
	]
	section_no = models.CharField(primary_key=True, max_length=10)
	sec = models.IntegerField(default=1)
	year = models.IntegerField(default=2020)
	semester = models.CharField(max_length=15, default='None', choices=SEMESTER)
	weekday = models.CharField(max_length=10, default='None', choices=WEEKDAY)
	start = models.CharField(max_length=10, default='None')
	end = models.CharField(max_length=10, default='None')
	current_enrollment = models.IntegerField(default=0, validators=[MaxValueValidator(30),MinValueValidator(0)])
	max_enrollment = models.IntegerField(default=30,validators=[MaxValueValidator(30)])
	course_no = models.ForeignKey(Course, on_delete=models.CASCADE)
	staff_id = models.ForeignKey(User, on_delete=models.CASCADE)
	building_code = models.ForeignKey(Building, on_delete=models.CASCADE)

	def __str__(self):
		return str(self.course_no) + '-' + str(self.sec)

# userName added
class Student(models.Model):
	GENDER = [
		('Male', 'Male'),
		('Female', 'Female'),
		('Undecided', 'Undecided'),
	]
	student_id = models.IntegerField(primary_key=True)
	userName = models.ForeignKey(User, on_delete=models.CASCADE)
	ssn = models.CharField(max_length=10, default="0000000000")
	name = models.CharField(max_length=100, default="None")
	gender = models.CharField(max_length=10, choices=GENDER)
	address = models.CharField(max_length=80, default='None')
	phone_number = PhoneField(blank=True,E164_only=False)
	email = models.EmailField(max_length=254)
	dep_code = models.ForeignKey(Department, on_delete=models.CASCADE)

	def __str__(self):
		return self.name

# Similar to ddl
class Registration(models.Model):
	SEMESTER = [
		('Fall', 'Fall'),
		('Spring', 'Spring'),
	]
	semester = models.CharField(max_length=15, default='None', choices=SEMESTER)
	year = models.IntegerField()
	grade = models.DecimalField(max_digits=4, decimal_places=2, default=0.00)
	stud_id = models.ForeignKey(User, on_delete=models.CASCADE)
	course_no = models.ForeignKey(Course, on_delete=models.CASCADE)
	section_no = models.ForeignKey(Section, on_delete=models.CASCADE)
	staff = models.ForeignKey(Staff, on_delete=models.CASCADE)

	@property
	def num_grade(self):
		if self.grade == 'A':
			return 4
		elif self.grade == 'B':
			return 3
		elif self.grade == 'C':
			return 2
		elif self.grade == 'D':
			return 1
		else:
			return 0		


# Similar to ddl
class faculty_department(models.Model):
	staff_id = models.ForeignKey(Staff, on_delete=models.CASCADE)
	dep_code = models.ForeignKey(Department, on_delete=models.CASCADE)