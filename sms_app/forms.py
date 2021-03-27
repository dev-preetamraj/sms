from django import forms
from django.forms import ModelForm

from .views import Staff


class AddStaffForm(ModelForm):
    class Meta:
        model = Staff
        fields = '__all__'
