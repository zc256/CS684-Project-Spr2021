import django_filters
from .models import Course, Section, Registration

class CourseFilter(django_filters.FilterSet):
	class Meta:
		model = Course
		fields = '__all__'
		exclude = ['course_no', 'course_name', 'credit']

class SectionFilter(django_filters.FilterSet):
	class Meta:
		model = Section
		fields = '__all__'
		exclude = ['section_no', 'section_name', 'year', 'semester', 'weekday', 'start','end','current_enrollment', 'max_enrollment', 'staff_id','building_code']

class EnrollmentFilter(django_filters.FilterSet):
	class Meta:
		model = Registration
		fields = '__all__'
		exclude = ['semester','year','grade','course_no','section_no','staff']

class GradingFilter(django_filters.FilterSet):
	class Meta:
		model = Registration
		fields = '__all__'
		exclude = ['semester','year','grade', 'section_no', 'stud_id']