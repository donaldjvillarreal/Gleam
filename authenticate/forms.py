from django import forms
from django.contrib.auth.models import User
from authenticate.models import UserProfile

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'first_name', 'last_name',)

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
    	gender = forms.ChoiceField(choices=UserProfile.GENDER, widget=forms.RadioSelect)
        fields = ('picture', 'gender',)