from django.forms import ModelForm
from .models import Registration

class RegisterForm(ModelForm):
	class Meta:
		model = Registration
		fields = '__all__'
		# exclude = ['']
