from django.contrib import admin
from .models import *

admin.site.register(Department)
admin.site.register(Student)
admin.site.register(Staff)
admin.site.register(Course)
admin.site.register(Building)
admin.site.register(Section)
admin.site.register(Registration)
# admin.site.register(Student_Enrollment)
# admin.site.register(Room)
admin.site.register(faculty_department)