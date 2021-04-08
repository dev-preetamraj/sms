from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .views import Staff, Student


class RegisterUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1',
                  'password2', 'first_name', 'last_name']

        widgets = {
            'username': forms.TextInput(attrs={'class': 'input-material'}),
            'email': forms.EmailInput(attrs={'class': 'input-material'}),
            'password1': forms.TextInput(attrs={'class': 'input-material', 'type': 'password'}),
            'password2': forms.TextInput(attrs={'class': 'input-material', 'type': 'password'}),
            'first_name': forms.TextInput(attrs={'class': 'input-material'}),
            'last_name': forms.TextInput(attrs={'class': 'input-material'})
        }


class AddStaffForm(ModelForm):
    class Meta:
        model = Staff
        fields = '__all__'


class AddStudentForm(ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
