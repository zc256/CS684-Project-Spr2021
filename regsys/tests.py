from django.test import LiveServerTestCase
from django.contrib.auth.models import User, Group, AbstractUser
from .models import *
from selenium import webdriver
import random
import sys,argparse,csv

driver = webdriver.Chrome(executable_path=r'C:/webdrivers/chromedriver.exe') # to open the chromebrowser 

usr='admin'
pwd='TestUserAdmin123'
driver.get('http://localhost:8000/login/')
driver.find_element_by_id('username').send_keys(usr)
driver.find_element_by_id('password').send_keys(pwd)
driver.find_element_by_xpath("//input[@type='submit']").click()

with open ('sections.csv') as csv_file:
	csv_reader=csv.DictReader(csv_file,delimiter=',')
	line_count=0
	for row in csv_reader:
		driver.get('http://localhost:8000/admin/regsys/section/add/')
		Article1=row['section_no']
		Article2=row['sec']
		Article3=row['year']
		Article4=row['semester']
		Article5=row['weekday']
		Article6=row['start']
		Article7=row['end']
		Article8=row['current_enrollment']
		Article9=row['max_enrollment']
		Article10=row['course_no']
		Article11=row['staff_id']
		Article12=row['building_code']
		driver.find_element_by_id('id_section_no').send_keys(Article1)
		driver.find_element_by_id('id_sec').send_keys(Article2)
		driver.find_element_by_id('id_year').send_keys(Article3)
		driver.find_element_by_id('id_semester').send_keys(Article4)
		driver.find_element_by_id('id_weekday').send_keys(Article5)
		driver.find_element_by_id('id_start').send_keys(Article6)
		driver.find_element_by_id('id_end').send_keys(Article7)
		driver.find_element_by_id('id_current_enrollment').send_keys(Article8)
		driver.find_element_by_id('id_max_enrollment').send_keys(Article9)
		driver.find_element_by_id('id_course_no').send_keys(Article10)
		driver.find_element_by_id('id_staff_id').send_keys(Article11)
		driver.find_element_by_id('id_building_code').send_keys(Article12)
		driver.find_element_by_xpath("//input[@value='Save']").click()






# User can log in to site depending on credentials (i.e. Student)
class userLogin(LiveServerTestCase):
	def setUp(self):
		self.driver = webdriver.Chrome(executable_path=r'C:/webdrivers/chromedriver.exe') # to open the chromebrowser 
		super(userLogin, self).setUp()	
		
	def tearDown(self):
		self.driver.quit()
		super(userLogin, self).tearDown()

	def loginUser(self):
		with open ('singleUser.csv') as csv_file:
			csv_reader=csv.DictReader(csv_file,delimiter=',')
			line_count=0
			for row in csv_reader:
						Article1=row['user']
						Article2=row['pwd']
		csv_file.close()

		self.driver.get('http://localhost:8000/login/')
		self.driver.implicitly_wait(10)
		self.driver.find_element_by_id('username').send_keys(Article1)
		self.driver.find_element_by_id('password').send_keys(Article2)
		self.driver.find_element_by_xpath("//input[@type='submit']").click()

# Admin can log in to admin site given proper credentials (superuser+staff account)
class adminLogin(LiveServerTestCase):
	def setUp(self):
		self.driver = webdriver.Chrome(executable_path=r'C:/webdrivers/chromedriver.exe') # to open the chromebrowser 
		super(adminLogin, self).setUp()	
		
	def tearDown(self):
		self.driver.quit()
		super(adminLogin, self).tearDown()

	def loginAdmin(self):
		with open ('test.csv') as csv_file:
			csv_reader=csv.DictReader(csv_file,delimiter=',')
			line_count=0
			for row in csv_reader:
						Article1=row['user']
						Article2=row['pwd']
		csv_file.close()

		self.driver.get('http://localhost:8000/admin/')
		self.driver.implicitly_wait(10)
		self.driver.find_element_by_id('id_username').send_keys(Article1)
		self.driver.find_element_by_id('id_password').send_keys(Article2)
		self.driver.find_element_by_xpath("//input[@type='submit']").click()

# Admin can create a new user
class createUser(LiveServerTestCase):
	def setUp(self):
		self.driver = webdriver.Chrome(executable_path=r'C:/webdrivers/chromedriver.exe') # to open the chromebrowser 
		super(createUser, self).setUp()	
		
	def tearDown(self):
		self.driver.quit()
		super(createUser, self).tearDown()

	def create(self):
		with open ('test.csv') as csv_file:
			csv_reader=csv.DictReader(csv_file,delimiter=',')
			line_count=0
			for row in csv_reader:
						Article1=row['user']
						Article2=row['pwd']
		csv_file.close()

		self.driver.get('http://localhost:8000/admin/')
		self.driver.implicitly_wait(10)
		self.driver.find_element_by_id('id_username').send_keys(Article1)
		self.driver.find_element_by_id('id_password').send_keys(Article2)
		self.driver.find_element_by_xpath("//input[@type='submit']").click()		

		self.driver.get('http://localhost:8000/admin/auth/user/add/')

		self.driver.find_element_by_id("id_username").send_keys("testUser3")
		self.driver.find_element_by_id("id_password1").send_keys("PassT3st123!")
		self.driver.find_element_by_id("id_password2").send_keys("PassT3st123!")
		self.driver.find_element_by_id("user_form").submit()

# Admin can delete a given user
class deleteUser(LiveServerTestCase):
	def setUp(self):
		self.driver = webdriver.Chrome(executable_path=r'C:/webdrivers/chromedriver.exe') # to open the chromebrowser 
		super(deleteUser, self).setUp()	
		
	def tearDown(self):
		self.driver.quit()
		super(deleteUser, self).tearDown()

	def deleteChoice(self):
		with open ('test.csv') as csv_file:
			csv_reader=csv.DictReader(csv_file,delimiter=',')
			line_count=0
			for row in csv_reader:
						Article1=row['user']
						Article2=row['pwd']
		csv_file.close()

		self.driver.get('http://localhost:8000/admin/')
		self.driver.find_element_by_id('id_username').send_keys(Article1)
		self.driver.find_element_by_id('id_password').send_keys(Article2)
		self.driver.find_element_by_xpath("//input[@type='submit']").click()		

		self.driver.get('http://localhost:8000/admin/auth/user/')
		self.driver.find_element_by_link_text('testUser3').click()
		self.driver.find_element_by_link_text('Delete').click()
		self.driver.find_element_by_xpath("//input[@value='Yes, I’m sure']").click()

# Admin can change group affiliation of user to Student
class changeUserGroupStudent(LiveServerTestCase):
	def setUp(self):
		self.driver = webdriver.Chrome(executable_path=r'C:/webdrivers/chromedriver.exe') # to open the chromebrowser 
		super(changeUserGroupStudent, self).setUp()	
		
	def tearDown(self):
		self.driver.quit()
		super(changeUserGroupStudent, self).tearDown()

	def create(self):
		with open ('test.csv') as csv_file:
			csv_reader=csv.DictReader(csv_file,delimiter=',')
			line_count=0
			for row in csv_reader:
						Article1=row['user']
						Article2=row['pwd']
		csv_file.close()

		self.driver.get('http://localhost:8000/admin/')
		self.driver.find_element_by_id('id_username').send_keys(Article1)
		self.driver.find_element_by_id('id_password').send_keys(Article2)
		self.driver.find_element_by_xpath("//input[@type='submit']").click()		

		self.driver.get('http://localhost:8000/admin/auth/user/add/')
		self.driver.find_element_by_id("id_username").send_keys("testUser3")
		self.driver.find_element_by_id("id_password1").send_keys("PassT3st123!")
		self.driver.find_element_by_id("id_password2").send_keys("PassT3st123!")
		self.driver.find_element_by_id("user_form").submit()

		self.driver.get('http://localhost:8000/admin/auth/user/')
		self.driver.find_element_by_link_text('testUser3').click()

		self.driver.find_element_by_xpath("//option[@value='1']").click()
		self.driver.find_element_by_id('id_groups_add_link').click()
		self.driver.find_element_by_id("user_form").submit()

# Admin can change group affiliation of user to Faculty
class changeUserGroupFaculty(LiveServerTestCase):
	def setUp(self):
		self.driver = webdriver.Chrome(executable_path=r'C:/webdrivers/chromedriver.exe') # to open the chromebrowser 
		super(changeUserGroupFaculty, self).setUp()	
		
	def tearDown(self):
		self.driver.quit()
		super(changeUserGroupFaculty, self).tearDown()

	def create(self):
		with open ('test.csv') as csv_file:
			csv_reader=csv.DictReader(csv_file,delimiter=',')
			line_count=0
			for row in csv_reader:
						Article1=row['user']
						Article2=row['pwd']
		csv_file.close()

		self.driver.get('http://localhost:8000/admin/')
		self.driver.find_element_by_id('id_username').send_keys(Article1)
		self.driver.find_element_by_id('id_password').send_keys(Article2)
		self.driver.find_element_by_xpath("//input[@type='submit']").click()		

		self.driver.get('http://localhost:8000/admin/auth/user/add/')
		self.driver.implicitly_wait(10)
		self.driver.find_element_by_id("id_username").send_keys("testUser4")
		self.driver.find_element_by_id("id_password1").send_keys("PassT3st123!")
		self.driver.find_element_by_id("id_password2").send_keys("PassT3st123!")
		self.driver.find_element_by_id("user_form").submit()

		self.driver.get('http://localhost:8000/admin/auth/user/')
		self.driver.find_element_by_link_text('testUser4').click()

		self.driver.find_element_by_xpath("//option[@value='2']").click()
		self.driver.find_element_by_id('id_groups_add_link').click()
		self.driver.find_element_by_id("user_form").submit()

# Admin can change the password of a given user
class adminChangeUserPassword(LiveServerTestCase):
	def setUp(self):
		self.driver = webdriver.Chrome(executable_path=r'C:/webdrivers/chromedriver.exe') # to open the chromebrowser 
		super(adminChangeUserPassword, self).setUp()	
		
	def tearDown(self):
		self.driver.quit()
		super(adminChangeUserPassword, self).tearDown()
	
	def changePassword(self):
		with open ('test.csv') as csv_file:
			csv_reader=csv.DictReader(csv_file,delimiter=',')
			line_count=0
			for row in csv_reader:
						Article1=row['user']
						Article2=row['pwd']
		csv_file.close()

		self.driver.get('http://localhost:8000/admin/')
		self.driver.find_element_by_id('id_username').send_keys(Article1)
		self.driver.find_element_by_id('id_password').send_keys(Article2)
		self.driver.find_element_by_xpath("//input[@type='submit']").click()		

		self.driver.get('http://localhost:8000/admin/auth/user/')
		self.driver.find_element_by_link_text('testUser3').click()	

		self.driver.find_element_by_link_text('this form').click()

		new_pass = 'Test_User_Password'
		password1 = self.driver.find_element_by_id('id_password1').send_keys(new_pass)
		password2 = self.driver.find_element_by_id('id_password2').send_keys(new_pass)
		self.driver.find_element_by_id("user_form").submit()

class adminGivePermissionsFaculty(LiveServerTestCase):
	def setUp(self):
		self.driver = webdriver.Chrome(executable_path=r'C:/webdrivers/chromedriver.exe') # to open the chromebrowser 
		super(adminGivePermissionsFaculty, self).setUp()	
		
	def tearDown(self):
		self.driver.quit()
		super(adminGivePermissionsFaculty, self).tearDown()

	def permissionsFaculty(self):
		with open ('test.csv') as csv_file:
			csv_reader=csv.DictReader(csv_file,delimiter=',')
			line_count=0
			for row in csv_reader:
						Article1=row['user']
						Article2=row['pwd']
		csv_file.close()

		self.driver.get('http://localhost:8000/admin/')
		self.driver.find_element_by_id('id_username').send_keys(Article1)
		self.driver.find_element_by_id('id_password').send_keys(Article2)
		self.driver.find_element_by_xpath("//input[@type='submit']").click()		

		self.driver.get('http://localhost:8000/admin/auth/group/')
		self.driver.find_element_by_link_text('Faculty').click()

		choose = self.driver.find_element_by_id('id_permissions_add_link')
		self.driver.find_element_by_xpath("//option[@value='4']").click()
		choose.click()
		self.driver.find_element_by_xpath("//option[@value='12']").click()
		choose.click()
		self.driver.find_element_by_xpath("//option[@value='16']").click()
		choose.click()
		self.driver.find_element_by_xpath("//option[@value='20']").click()
		choose.click()
		self.driver.find_element_by_xpath("//option[@value='24']").click()
		choose.click()
		self.driver.find_element_by_id("group_form").submit()

class studentAccessProfile(LiveServerTestCase):
	def setUp(self):
		self.driver = webdriver.Chrome(executable_path=r'C:/webdrivers/chromedriver.exe') # to open the chromebrowser 
		super(studentAccessProfile, self).setUp()	
		
	def tearDown(self):
		self.driver.quit()
		super(studentAccessProfile, self).tearDown()

	def accessProf(self):
		with open ('singleUser.csv') as csv_file:
			csv_reader=csv.DictReader(csv_file,delimiter=',')
			line_count=0
			for row in csv_reader:
						Article1=row['user']
						Article2=row['pwd']
		csv_file.close()
		self.driver.get('http://localhost:8000/login/')

		self.driver.find_element_by_id('username').send_keys(Article1)
		self.driver.find_element_by_id('password').send_keys(Article2)
		self.driver.find_element_by_xpath("//input[@type='submit']").click()
		self.driver.get('http://localhost:8000/studentprof/')

class studentEditProfile(LiveServerTestCase):
	def setUp(self):
		self.driver = webdriver.Chrome(executable_path=r'C:/webdrivers/chromedriver.exe') # to open the chromebrowser 
		super(studentEditProfile, self).setUp()	
		
	def tearDown(self):
		self.driver.quit()
		super(studentEditProfile, self).tearDown()

	def editProf(self):
		with open ('singleUser.csv') as csv_file:
			csv_reader=csv.DictReader(csv_file,delimiter=',')
			line_count=0
			for row in csv_reader:
						Article1=row['user']
						Article2=row['pwd']
		csv_file.close()
		self.driver.get('http://localhost:8000/login/')

		self.driver.find_element_by_id('username').send_keys(Article1)
		self.driver.find_element_by_id('password').send_keys(Article2)
		self.driver.find_element_by_xpath("//input[@type='submit']").click()

		self.driver.get('http://localhost:8000/studentprof/')
		self.driver.find_element_by_xpath("//a[@href='/editinfo/']").click()

		stud_id = 1
		address = 'Test Address'

		stud_id = self.driver.find_element_by_id('student_id').send_keys(stud_id)
		address = self.driver.find_element_by_id('address').send_keys(address)

		submit = self.driver.find_element_by_xpath("//input[@type='submit']")
		submit.click()

class studentAccessCatalog(LiveServerTestCase):
	def setUp(self):
		self.driver = webdriver.Chrome(executable_path=r'C:/webdrivers/chromedriver.exe') # to open the chromebrowser 
		super(studentAccessCatalog, self).setUp()	
		
	def tearDown(self):
		self.driver.quit()
		super(studentAccessCatalog, self).tearDown()

	def accessCatalog(self):
		with open ('singleUser.csv') as csv_file:
			csv_reader=csv.DictReader(csv_file,delimiter=',')
			line_count=0
			for row in csv_reader:
						Article1=row['user']
						Article2=row['pwd']
		csv_file.close()
		self.driver.get('http://localhost:8000/login/')
		self.driver.implicitly_wait(10)

		self.driver.find_element_by_id('username').send_keys(Article1)
		self.driver.find_element_by_id('password').send_keys(Article2)
		self.driver.find_element_by_xpath("//input[@type='submit']").click()

		self.driver.get('http://localhost:8000/catalog/')

class studentFilterCatalog(LiveServerTestCase):
	def setUp(self):
		self.driver = webdriver.Chrome(executable_path=r'C:/webdrivers/chromedriver.exe') # to open the chromebrowser 
		super(studentFilterCatalog, self).setUp()	
		
	def tearDown(self):
		self.driver.quit()
		super(studentFilterCatalog, self).tearDown()

	def filterCatalog(self):
		with open ('singleUser.csv') as csv_file:
			csv_reader=csv.DictReader(csv_file,delimiter=',')
			line_count=0
			for row in csv_reader:
						Article1=row['user']
						Article2=row['pwd']
		csv_file.close()
		self.driver.get('http://localhost:8000/login/')

		self.driver.find_element_by_id('username').send_keys(Article1)
		self.driver.find_element_by_id('password').send_keys(Article2)
		self.driver.find_element_by_xpath("//input[@type='submit']").click()

		self.driver.get('http://localhost:8000/catalog/')
		self.driver.find_element_by_id("id_course_no").click()
		self.driver.find_element_by_xpath("//option[@value='CS 101']").click()
		self.driver.find_element_by_xpath("//button[@type='submit']").click()

class studentFilterAdd(LiveServerTestCase):
	def setUp(self):
		self.driver = webdriver.Chrome(executable_path=r'C:/webdrivers/chromedriver.exe') # to open the chromebrowser 
		super(studentFilterAdd, self).setUp()	
		
	def tearDown(self):
		self.driver.quit()
		super(studentFilterAdd, self).tearDown()

	def filterAdd(self):
		with open ('singleUser.csv') as csv_file:
			csv_reader=csv.DictReader(csv_file,delimiter=',')
			line_count=0
			for row in csv_reader:
						Article1=row['user']
						Article2=row['pwd']
		csv_file.close()
		self.driver.get('http://localhost:8000/login/')

		self.driver.find_element_by_id('username').send_keys(Article1)
		self.driver.find_element_by_id('password').send_keys(Article2)
		self.driver.find_element_by_xpath("//input[@type='submit']").click()

		self.driver.get('http://localhost:8000/catalog/')
		self.driver.find_element_by_id("id_course_no").click()
		self.driver.find_element_by_xpath("//option[@value='CS 101']").click()
		self.driver.find_element_by_xpath("//button[@type='submit']").click()

		self.driver.find_element_by_xpath("//a[@class='btn btn-sm btn-info']").click()

class studentDropCourse(LiveServerTestCase):
	def setUp(self):
		self.driver = webdriver.Chrome(executable_path=r'C:/webdrivers/chromedriver.exe') # to open the chromebrowser 
		super(studentDropCourse, self).setUp()	
		
	def tearDown(self):
		self.driver.quit()
		super(studentDropCourse, self).tearDown()

	def dropCourse(self):
		with open ('singleUser.csv') as csv_file:
			csv_reader=csv.DictReader(csv_file,delimiter=',')
			line_count=0
			for row in csv_reader:
						Article1=row['user']
						Article2=row['pwd']
		csv_file.close()
		self.driver.get('http://localhost:8000/login/')

		self.driver.find_element_by_id('username').send_keys(Article1)
		self.driver.find_element_by_id('password').send_keys(Article2)
		self.driver.find_element_by_xpath("//input[@type='submit']").click()

		self.driver.get('http://localhost:8000/schedule/')
		self.driver.find_element_by_xpath("//a[@class='btn btn-sm btn-info']").click()
		self.driver.find_element_by_xpath("//input[@type='submit']").click()

class studentViewTranscript(LiveServerTestCase):
	def setUp(self):
		self.driver = webdriver.Chrome(executable_path=r'C:/webdrivers/chromedriver.exe') # to open the chromebrowser 
		super(studentViewTranscript, self).setUp()	
		
	def tearDown(self):
		self.driver.quit()
		super(studentViewTranscript, self).tearDown()

	def viewTranscript(self):
		with open ('singleUser.csv') as csv_file:
			csv_reader=csv.DictReader(csv_file,delimiter=',')
			line_count=0
			for row in csv_reader:
						Article1=row['user']
						Article2=row['pwd']
		csv_file.close()
		self.driver.get('http://localhost:8000/login/')

		self.driver.find_element_by_id('username').send_keys(Article1)
		self.driver.find_element_by_id('password').send_keys(Article2)
		self.driver.find_element_by_xpath("//input[@type='submit']").click()
		self.driver.get('http://localhost:8000/transcript/')

class adminViewEnrollment(LiveServerTestCase):
	def setUp(self):
		self.driver = webdriver.Chrome(executable_path=r'C:/webdrivers/chromedriver.exe') # to open the chromebrowser 
		super(adminViewEnrollment, self).setUp()	
		
	def tearDown(self):
		self.driver.quit()
		super(adminViewEnrollment, self).tearDown()

	def viewEnroll(self):
		with open ('test.csv') as csv_file:
			csv_reader=csv.DictReader(csv_file,delimiter=',')
			line_count=0
			for row in csv_reader:
						Article1=row['user']
						Article2=row['pwd']
		csv_file.close()

		self.driver.get('http://localhost:8000/login/')

		self.driver.find_element_by_id('username').send_keys(Article1)
		self.driver.find_element_by_id('password').send_keys(Article2)
		self.driver.find_element_by_xpath("//input[@type='submit']").click()
		self.driver.get('http://localhost:8000/enrollment/')

class adminFilterEnrollment(LiveServerTestCase):
	def setUp(self):
		self.driver = webdriver.Chrome(executable_path=r'C:/webdrivers/chromedriver.exe') # to open the chromebrowser 
		super(adminFilterEnrollment, self).setUp()	
		
	def tearDown(self):
		self.driver.quit()
		super(adminFilterEnrollment, self).tearDown()

	def filterEnroll(self):
		with open ('test.csv') as csv_file:
			csv_reader=csv.DictReader(csv_file,delimiter=',')
			line_count=0
			for row in csv_reader:
						Article1=row['user']
						Article2=row['pwd']
		csv_file.close()

		self.driver.get('http://localhost:8000/login/')
		self.driver.implicitly_wait(10)

		self.driver.find_element_by_id('username').send_keys(Article1)
		self.driver.find_element_by_id('password').send_keys(Article2)

		self.driver.find_element_by_xpath("//input[@type='submit']").click()

		self.driver.get('http://localhost:8000/enrollment/')

		self.driver.find_element_by_id("id_stud_id").click()
		self.driver.find_element_by_xpath("//option[@value='3']").click()
		self.driver.find_element_by_xpath("//button[@type='submit']").click()

		self.driver.find_element_by_id("id_stud_id").click()
		self.driver.find_element_by_xpath("//option[@value='4']").click()
		self.driver.find_element_by_xpath("//button[@type='submit']").click()

class adminViewStats(LiveServerTestCase):
	def setUp(self):
		self.driver = webdriver.Chrome(executable_path=r'C:/webdrivers/chromedriver.exe') # to open the chromebrowser 
		super(adminViewStats, self).setUp()	
		
	def tearDown(self):
		self.driver.quit()
		super(adminViewStats, self).tearDown()

	def viewStats(self):
		with open ('test.csv') as csv_file:
			csv_reader=csv.DictReader(csv_file,delimiter=',')
			line_count=0
			for row in csv_reader:
						Article1=row['user']
						Article2=row['pwd']
		csv_file.close()

		self.driver.get('http://localhost:8000/login/')

		self.driver.find_element_by_id('username').send_keys(Article1)
		self.driver.find_element_by_id('password').send_keys(Article2)
		self.driver.find_element_by_xpath("//input[@type='submit']").click()
		self.driver.get('http://localhost:8000/statistics/')

class adminViewStaff(LiveServerTestCase):
	def setUp(self):
		self.driver = webdriver.Chrome(executable_path=r'C:/webdrivers/chromedriver.exe') # to open the chromebrowser 
		super(adminViewStaff, self).setUp()	
		
	def tearDown(self):
		self.driver.quit()
		super(adminViewStaff, self).tearDown()

	def viewStaff(self):
		with open ('test.csv') as csv_file:
			csv_reader=csv.DictReader(csv_file,delimiter=',')
			line_count=0
			for row in csv_reader:
						Article1=row['user']
						Article2=row['pwd']
		csv_file.close()

		self.driver.get('http://localhost:8000/login/')

		self.driver.find_element_by_id('username').send_keys(Article1)
		self.driver.find_element_by_id('password').send_keys(Article2)
		self.driver.find_element_by_xpath("//input[@type='submit']").click()
		self.driver.get('http://localhost:8000/staff/')

class adminViewStudents(LiveServerTestCase):
	def setUp(self):
		self.driver = webdriver.Chrome(executable_path=r'C:/webdrivers/chromedriver.exe') # to open the chromebrowser 
		super(adminViewStudents, self).setUp()	
		
	def tearDown(self):
		self.driver.quit()
		super(adminViewStudents, self).tearDown()

	def viewStudents(self):
		with open ('test.csv') as csv_file:
			csv_reader=csv.DictReader(csv_file,delimiter=',')
			line_count=0
			for row in csv_reader:
						Article1=row['user']
						Article2=row['pwd']
		csv_file.close()

		self.driver.get('http://localhost:8000/login/')

		self.driver.find_element_by_id('username').send_keys(Article1)
		self.driver.find_element_by_id('password').send_keys(Article2)
		self.driver.find_element_by_xpath("//input[@type='submit']").click()
		self.driver.get('http://localhost:8000/students/')

class failAdminLogin(LiveServerTestCase):
	def setUp(self):
		self.driver = webdriver.Chrome(executable_path=r'C:/webdrivers/chromedriver.exe') # to open the chromebrowser 
		super(failAdminLogin, self).setUp()	
		
	def tearDown(self):
		self.driver.quit()
		super(failAdminLogin, self).tearDown()

	def failLogin(self):
		with open ('test.csv') as csv_file:
			csv_reader=csv.DictReader(csv_file,delimiter=',')
			line_count=0
			for row in csv_reader:
						Article1=row['user']
						Article2=row['pwd']
		csv_file.close()	

		self.driver.get('http://localhost:8000/admin/')
		self.driver.find_element_by_id('id_username').send_keys(Article1)
		self.driver.find_element_by_id('id_password').send_keys(Article2)
		self.driver.find_element_by_xpath("//input[@type='submit']").click()		
		self.driver.get('http://localhost:8000/admin/auth/group/')

class deleteSection(LiveServerTestCase):
	def setUp(self):
		self.driver = webdriver.Chrome(executable_path=r'C:/webdrivers/chromedriver.exe') # to open the chromebrowser 
		super(deleteSection, self).setUp()	
		
	def tearDown(self):
		self.driver.quit()
		super(deleteSection, self).tearDown()

	def delSec(self):
		with open ('test.csv') as csv_file:
			csv_reader=csv.DictReader(csv_file,delimiter=',')
			line_count=0
			for row in csv_reader:
						Article1=row['user']
						Article2=row['pwd']
		csv_file.close()

		self.driver.get('http://localhost:8000/login/')
		self.driver.find_element_by_id('username').send_keys(Article1)
		self.driver.find_element_by_id('password').send_keys(Article2)
		self.driver.find_element_by_xpath("//input[@type='submit']").click()

		self.driver.get('http://localhost:8000/deletesection/')
		self.driver.find_element_by_id('cno').send_keys('CS 101')
		self.driver.find_element_by_id('sno').send_keys('2')
		self.driver.find_element_by_xpath("//input[@type='submit']").click()	

class deleteCourse(LiveServerTestCase):
	def setUp(self):
		self.driver = webdriver.Chrome(executable_path=r'C:/webdrivers/chromedriver.exe') # to open the chromebrowser 
		super(deleteCourse, self).setUp()	
		
	def tearDown(self):
		self.driver.quit()
		super(deleteCourse, self).tearDown()

	def delCor(self):
		with open ('test.csv') as csv_file:
			csv_reader=csv.DictReader(csv_file,delimiter=',')
			line_count=0
			for row in csv_reader:
						Article1=row['user']
						Article2=row['pwd']
		csv_file.close()

		self.driver.get('http://localhost:8000/login/')
		self.driver.find_element_by_id('username').send_keys(Article1)
		self.driver.find_element_by_id('password').send_keys(Article2)
		self.driver.find_element_by_xpath("//input[@type='submit']").click()

		self.driver.get('http://localhost:8000/deletecourse/')
		self.driver.find_element_by_id('cno').send_keys('CS 101')
		self.driver.find_element_by_xpath("//input[@type='submit']").click()		

class multUsers(LiveServerTestCase):
	def setUp(self):
		self.driver = webdriver.Chrome(executable_path=r'C:/webdrivers/chromedriver.exe') # to open the chromebrowser 
		super(multUsers, self).setUp()	
		
	def tearDown(self):
		self.driver.quit()
		super(multUsers, self).tearDown()

	def loginMult(self):
		with open ('testUser.csv') as csv_file:
			csv_reader=csv.DictReader(csv_file,delimiter=',')
			line_count=0
			for row in csv_reader:
				Article1=row['user']
				Article2=row['pwd']
				self.driver.get('http://localhost:8000/login/')
				self.driver.find_element_by_id('username').send_keys(Article1)
				self.driver.find_element_by_id('password').send_keys(Article2)
				self.driver.find_element_by_xpath("//input[@type='submit']").click()
				self.driver.get('http://localhost:8000/logout/')
		csv_file.close()


class multUserProf(LiveServerTestCase):
	def setUp(self):
		self.driver = webdriver.Chrome(executable_path=r'C:/webdrivers/chromedriver.exe') # to open the chromebrowser 
		super(multUserProf, self).setUp()	
		
	def tearDown(self):
		self.driver.quit()
		super(multUserProf, self).tearDown()

	def multProf(self):
		with open ('testUser.csv') as csv_file:
			csv_reader=csv.DictReader(csv_file,delimiter=',')
			line_count=0
			for row in csv_reader:
				Article1=row['user']
				Article2=row['pwd']
				self.driver.get('http://localhost:8000/login/')
				self.driver.find_element_by_id('username').send_keys(Article1)
				self.driver.find_element_by_id('password').send_keys(Article2)
				self.driver.find_element_by_xpath("//input[@type='submit']").click()
				self.driver.get('http://localhost:8000/studentprof/')
				self.driver.get('http://localhost:8000/logout/')
		csv_file.close()


class sections(LiveServerTestCase):
	def setUp(self):
		self.driver = webdriver.Chrome(executable_path=r'C:/webdrivers/chromedriver.exe') # to open the chromebrowser 
		super(sections, self).setUp()	
		
	def tearDown(self):
		self.driver.quit()
		super(sections, self).tearDown()

	def sec(self):
		usr='admin'
		pwd='testAdmin123'
		self.driver.get('http://localhost:8000/login/')
		self.driver.find_element_by_id('username').send_keys(usr)
		self.driver.find_element_by_id('password').send_keys(pwd)
		self.driver.find_element_by_xpath("//input[@type='submit']").click()
		self.driver.get('http://localhost:8000/admin/regsys/section/add/')
		
		with open ('sections.csv') as csv_file:
			csv_reader=csv.DictReader(csv_file,delimiter=',')
			line_count=0
			for row in csv_reader:
				Article1=row['section_no']
				Article2=row['sec']
				Article3=row['year']
				Article4=row['semester']
				Article5=row['weekday']
				Article6=row['start']
				Article7=row['end']
				Article8=row['current_enrollment']
				Article9=row['max_enrollment']
				Article10=row['course_no']
				Article11=row['staff_id']
				Article12=row['building_code']
				self.driver.find_element_by_id('id_section_no').send_keys(Article1)
				self.driver.find_element_by_id('id_sec').send_keys(Article2)
				self.driver.find_element_by_id('id_year').send_keys(Article3)
				self.driver.find_element_by_id('id_semester').send_keys(Article4)
				self.driver.find_element_by_id('id_weekday').send_keys(Article5)
				self.driver.find_element_by_id('id_start').send_keys(Article6)
				self.driver.find_element_by_id('id_end').send_keys(Article7)
				self.driver.find_element_by_id('id_current_enrollment').send_keys(Article8)
				self.driver.find_element_by_id('id_max_enrollment').send_keys(Article9)
				self.driver.find_element_by_id('id_course_no').send_keys(Article10)
				self.driver.find_element_by_id('id_staff_id').send_keys(Article11)
				self.driver.find_element_by_id('id_building_code').send_keys(Article12)

		csv_file.close()

		