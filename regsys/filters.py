import django_filters
from .models import Course, Section

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