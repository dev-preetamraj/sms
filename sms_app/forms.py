from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# from .views import Staff, Student
from .models import Course, Staff, Student, Subject, SessionYear, Students_FeedBack


class RegisterUserForm(UserCreationForm):
    USERTYPE = (
        ('hod', 'hod'),
        ('staff', 'staff'),
        ('student', 'student')
    )
    GENDER = (('Male', 'Male'),('Female', 'Female'),('Other', 'Other'))
    user_type = forms.ChoiceField(choices=USERTYPE)
    gender = forms.ChoiceField(choices=GENDER)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1',
                  'password2', 'first_name', 'last_name','gender', 'user_type']

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

class AddCourseForm(ModelForm):
    class Meta:
        model = Course
        fields = '__all__'

class AddSubjectForm(ModelForm):
    class Meta:
        model = Subject
        fields = '__all__'

class AddSessionForm(ModelForm):
    class Meta:
        model = SessionYear
        fields = '__all__'


class UpdateUserForm(ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name']




#Students Templates Form ===========================================================================
#Students Templates Form ===========================================================================

class StudentLeaveForm(ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

class StudentFeedbackForm(ModelForm):
    class Meta:
        model = Students_FeedBack
        fields = ['student_id', 'feedback']

