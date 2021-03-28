from django.test import LiveServerTestCase
from django.contrib.auth.models import User, Group, AbstractUser
from .models import *
from selenium import webdriver
import random
import csv

f_name = ['John', 'Maria', 'Bob', 'Steve', 'Nicole', 'Lauren', 'Zach', 'Rebecca']
l_name = ['Stevens', 'O\'Brien', 'McDonald','Rodriguez','Davis']
dep = ['CS', 'IT']
num = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
id = random.randint(100000,999999)

i = 0
while i <= 3:
	firstName = str(random.choice(f_name))
	lastName = str(random.choice(l_name))
	name = firstName[0] + '' + lastName[0] + '' + str(random.choice(num))
	stud_id = id
	depC = Department.objects.get(dep_code=random.choice(dep))
	email = name + '@gmail.com'
	password = 'TestStudent1234'

	user = User.objects.create_user(name, email, password)
	user.first_name = firstName
	user.last_name = lastName
	user.save()
	
	
	student = Group.objects.get(name='Student') 
	student.user_set.add(user)

	s = Student(student_id=stud_id, userName=user, ssn=0000000000, name=user.first_name+ ' '+user.last_name, gender='Male', address='Test', mob_no='1234567890', email=user.email, dep_code=depC)
	s.pk = None
	s.save() 

	i +=1

# User can log in to site depending on credentials (i.e. Student)
class userLogin(LiveServerTestCase):
	def setUp(self):
		self.driver = webdriver.Chrome(executable_path=r'C:/webdrivers/chromedriver.exe') # to open the chromebrowser 
		super(userLogin, self).setUp()	
		
	def tearDown(self):
		self.driver.quit()
		super(userLogin, self).tearDown()

	def loginUser(self):
		username = 'newUser2'
		password = 'TestPassword123'

		self.driver.get('http://localhost:8000/login/')
		self.driver.implicitly_wait(10)
		user_input = self.driver.find_element_by_id('username')
		user_input.send_keys(username)
		password_input = self.driver.find_element_by_id('password')
		password_input.send_keys(password)
		login_btn = self.driver.find_element_by_xpath("//input[@type='submit']")
		login_btn.click()


# Student user can access student profile page
class selectStudentProfile(LiveServerTestCase):
	def setUp(self):
		self.driver = webdriver.Chrome(executable_path=r'C:/webdrivers/chromedriver.exe') # to open the chromebrowser 
		super(selectStudentProfile, self).setUp()	
		
	def tearDown(self):
		self.driver.quit()
		super(selectStudentProfile, self).tearDown()
	
	def profile(self):
		username = 'newUser2'
		password = 'TestPassword123'
		self.driver.get('http://localhost:8000/login/')
		self.driver.implicitly_wait(10)

		user_input = self.driver.find_element_by_id('username')
		user_input.send_keys(username)
		password_input = self.driver.find_element_by_id('password')
		password_input.send_keys(password)

		login_btn = self.driver.find_element_by_xpath("//input[@type='submit']")
		login_btn.click()
		self.driver.get('http://localhost:8000/studentprof/')

# Admin can log in to admin site given proper credentials (superuser+staff account)
class adminLogin(LiveServerTestCase):
	def setUp(self):
		self.driver = webdriver.Chrome(executable_path=r'C:/webdrivers/chromedriver.exe') # to open the chromebrowser 
		super(adminLogin, self).setUp()	
		
	def tearDown(self):
		self.driver.quit()
		super(adminLogin, self).tearDown()

	def loginAdmin(self):
		username = 'admin2'
		password = 'testAdmin321'

		self.driver.get('http://localhost:8000/admin/')
		self.driver.implicitly_wait(10)
		user_input = self.driver.find_element_by_id('id_username')
		user_input.send_keys(username)
		password_input = self.driver.find_element_by_id('id_password')
		password_input.send_keys(password)
		login_btn = self.driver.find_element_by_xpath("//input[@type='submit']")
		login_btn.click()


# Admin can create a new user
class createUser(LiveServerTestCase):
	def setUp(self):
		self.driver = webdriver.Chrome(executable_path=r'C:/webdrivers/chromedriver.exe') # to open the chromebrowser 
		super(createUser, self).setUp()	
		
	def tearDown(self):
		self.driver.quit()
		super(createUser, self).tearDown()

	def create(self):
		username = 'admin2'
		password = 'testAdmin321'

		self.driver.get('http://localhost:8000/admin/')
		self.driver.implicitly_wait(10)
		user_input = self.driver.find_element_by_id('id_username')
		user_input.send_keys(username)
		password_input = self.driver.find_element_by_id('id_password')
		password_input.send_keys(password)
		login_btn = self.driver.find_element_by_xpath("//input[@type='submit']")
		login_btn.click()		

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
		username = 'admin2'
		password = 'testAdmin321'

		self.driver.get('http://localhost:8000/admin/')
		self.driver.implicitly_wait(10)
		user_input = self.driver.find_element_by_id('id_username')
		user_input.send_keys(username)
		password_input = self.driver.find_element_by_id('id_password')
		password_input.send_keys(password)
		login_btn = self.driver.find_element_by_xpath("//input[@type='submit']")
		login_btn.click()		
		self.driver.implicitly_wait(10)

		self.driver.get('http://localhost:8000/admin/auth/user/')
		user_id = self.driver.find_element_by_link_text('testUser3') # input any user
		user_id.click()
		delete_link = self.driver.find_element_by_link_text('Delete')
		delete_link.click()
		confirm = self.driver.find_element_by_xpath("//input[@value='Yes, I’m sure']")
		confirm.click()


# Admin can change group affiliation of user to Student
class changeUserGroupStudent(LiveServerTestCase):
	def setUp(self):
		self.driver = webdriver.Chrome(executable_path=r'C:/webdrivers/chromedriver.exe') # to open the chromebrowser 
		super(changeUserGroupStudent, self).setUp()	
		
	def tearDown(self):
		self.driver.quit()
		super(changeUserGroupStudent, self).tearDown()

	def create(self):
		username = 'admin2'
		password = 'testAdmin321'

		self.driver.get('http://localhost:8000/admin/')
		self.driver.implicitly_wait(10)
		user_input = self.driver.find_element_by_id('id_username')
		user_input.send_keys(username)
		password_input = self.driver.find_element_by_id('id_password')
		password_input.send_keys(password)
		login_btn = self.driver.find_element_by_xpath("//input[@type='submit']")
		login_btn.click()		
		self.driver.implicitly_wait(10)

		self.driver.get('http://localhost:8000/admin/auth/user/')
		user_id = self.driver.find_element_by_link_text('newUser2') # input any user
		user_id.click()

		student = self.driver.find_element_by_xpath("//option[@value='1']")
		student.click()
		choose = self.driver.find_element_by_id('id_groups_add_link')
		choose.click()
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
		username = 'admin2'
		password = 'testAdmin321'

		self.driver.get('http://localhost:8000/admin/')
		self.driver.implicitly_wait(10)
		user_input = self.driver.find_element_by_id('id_username')
		user_input.send_keys(username)
		password_input = self.driver.find_element_by_id('id_password')
		password_input.send_keys(password)
		login_btn = self.driver.find_element_by_xpath("//input[@type='submit']")
		login_btn.click()		
		self.driver.implicitly_wait(10)

		self.driver.get('http://localhost:8000/admin/auth/user/')
		user_id = self.driver.find_element_by_link_text('newUser2') # input any user
		user_id.click()

		student = self.driver.find_element_by_xpath("//option[@value='2']")
		student.click()
		choose = self.driver.find_element_by_id('id_groups_add_link')
		choose.click()
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
		username = 'admin2'
		password = 'testAdmin321'

		self.driver.get('http://localhost:8000/admin/')
		self.driver.implicitly_wait(10)
		user_input = self.driver.find_element_by_id('id_username')
		user_input.send_keys(username)
		password_input = self.driver.find_element_by_id('id_password')
		password_input.send_keys(password)
		login_btn = self.driver.find_element_by_xpath("//input[@type='submit']")
		login_btn.click()		

		self.driver.get('http://localhost:8000/admin/auth/user/')
		user_id = self.driver.find_element_by_link_text('newUser2') # input any user
		user_id.click()	

		this_form = self.driver.find_element_by_link_text('this form')
		this_form.click()

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
		username = 'admin2'
		password = 'testAdmin321'

		self.driver.get('http://localhost:8000/admin/')
		self.driver.implicitly_wait(10)
		user_input = self.driver.find_element_by_id('id_username')
		user_input.send_keys(username)
		password_input = self.driver.find_element_by_id('id_password')
		password_input.send_keys(password)
		login_btn = self.driver.find_element_by_xpath("//input[@type='submit']")
		login_btn.click()		
		self.driver.implicitly_wait(10)

		self.driver.get('http://localhost:8000/admin/auth/group/')
		faculty_link = self.driver.find_element_by_link_text('Faculty')
		faculty_link.click()

		choose = self.driver.find_element_by_id('id_permissions_add_link')
		adminViewEntry = self.driver.find_element_by_xpath("//option[@value='4']")
		adminViewEntry.click()
		choose.click()
		authGroupView = self.driver.find_element_by_xpath("//option[@value='12']")
		authGroupView.click()
		choose.click()
		authUserView = self.driver.find_element_by_xpath("//option[@value='16']")
		authUserView.click()
		choose.click()
		contentViewContent = self.driver.find_element_by_xpath("//option[@value='20']")
		contentViewContent.click()
		choose.click()
		sessionViewSession = self.driver.find_element_by_xpath("//option[@value='24']")
		sessionViewSession.click()
		choose.click()
		self.driver.find_element_by_id("group_form").submit()