import django_filters
from .models import Course

class CourseFilter(django_filters.FilterSet):
	class Meta:
		model = Course
		fields = '__all__'
		exclude = ['course_num', 'course_name', 'description', 'credits']