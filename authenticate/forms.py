from django import forms
from django.contrib.auth.models import User
from authenticate.models import UserProfile
from passwords.fields import PasswordField

class UserForm(forms.ModelForm):
	username = forms.CharField(min_length=5, max_length=30, required=True)
	password = PasswordField(widget=forms.PasswordInput(),
	    						label='Password',
	    						required=True
	)

	password2 = forms.CharField(widget=forms.PasswordInput(),
	    						label='Password Confirmation',
	    						required=True
	)

	first_name = forms.CharField(max_length=20, required=True)
	last_name = forms.CharField(max_length=20, required=True)

	def clean_password2(self):
	    password = self.cleaned_data.get('password')
	    password2 = self.cleaned_data.get('password2')

	    if not password2:
	        raise forms.ValidationError("You must confirm your password")
	    if password != password2:
	        raise forms.ValidationError("Your passwords do not match")
	    return password2

	class Meta:
	    model = User
	    fields = ('username', 'email', 'password', 'password2', 'first_name', 'last_name',)

class UserProfileForm(forms.ModelForm):
	gender = forms.CharField(max_length=1, required=True)
	dob = forms.DateField(required=True)
	timezone = forms.IntegerField(widget=forms.HiddenInput())

	def clean_phone(self):
	    phone = self.cleaned_data.get('phone')
	    if len(phone) !=0 and len(phone) != 10:
	        raise forms.ValidationError("Phone number must be 10 digits long")
	    if len(phone) !=0 and not phone.isdigit():
	        raise forms.ValidationError("Phone number can only contain numbers")
	    return phone

	class Meta:
		model = UserProfile
		gender = forms.ChoiceField(choices=UserProfile.GENDER, widget=forms.RadioSelect)
		fields = ('picture','gender','phone','dob','timezone','subscribed',)