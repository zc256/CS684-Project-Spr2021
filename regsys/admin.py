from django.contrib import admin
from .models import *
# from django.contrib.auth import get_user_model
# from django.contrib.auth.admin import UserAdmin

admin.site.register(Department)
admin.site.register(Student)
admin.site.register(Staff)
admin.site.register(Course)
admin.site.register(Building)
admin.site.register(Section)
admin.site.register(Registration)
# admin.site.register(Student_Enrollment)
admin.site.register(Room)
admin.site.register(faculty_department)




# class MyUserAdmin(UserAdmin):
#     add_form = MyUserCreationForm
#     form = MyUserChangeForm
#     model = MyUser
#     list_display = ['username', 'mobile_number', 'birth_date']
#     fieldsets = UserAdmin.fieldsets + (
#             (None, {'fields': ('mobile_number', 'birth_date')}),
#     ) #this will allow to change these fields in admin module


# admin.site.register(MyUser, MyUserAdmin)
# # admin.site.register(Student)