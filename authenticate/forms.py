from django import forms
from django.contrib.auth.models import User
from authenticate.models import UserProfile

class UserForm(forms.ModelForm):
    #password = forms.CharField(widget=forms.PasswordInput())

	password = forms.CharField(widget=forms.PasswordInput(),
	    						label='Password'
	)
	password2 = forms.CharField(widget=forms.PasswordInput(),
	    						label='Password Confirmation'
	)

	first_name = forms.CharField(max_length=20, required=True)
	last_name = forms.CharField(max_length=20, required=True)

	class Meta:
	    model = User
	    fields = ('username', 'email', 'password', 'password2', 'first_name', 'last_name',)

class UserProfileForm(forms.ModelForm):
	gender = forms.CharField(max_length=1, required=True)
	dob = forms.DateField(required=True)
	timezone = forms.IntegerField(widget=forms.HiddenInput())

	class Meta:
		model = UserProfile
		gender = forms.ChoiceField(choices=UserProfile.GENDER, widget=forms.RadioSelect)
		fields = ('picture', 'gender', 'dob','timezone')