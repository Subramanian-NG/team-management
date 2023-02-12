from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from . models import Member

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ['username','email', 'password1','password2']

class CreateUserForm(ModelForm):
    class Meta:
        model = Member
        fields = '__all__'
        widgets = {'isAdmin': forms.RadioSelect(choices=[
            (True, 'Admin - Can delete members'),
            (False, 'Regular - Can\'t delete members')             
        ]),
        'firstname': forms.TextInput(attrs={'placeholder': 'First Name'}),
        'lastname': forms.TextInput(attrs={'placeholder': 'Last Name'}),
        'email': forms.TextInput(attrs={'placeholder': 'Email'}),
        'phone': forms.TextInput(attrs={'placeholder': 'Phone'}),
        }
        labels = {
            "isAdmin": "Role",
        }