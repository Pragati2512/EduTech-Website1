from django import forms
from .models import person, student, teacher, doubt
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "password", "email",  )


class RegisterForm(forms.ModelForm):
    class Meta:
        model = person
        fields = ("f_name", "l_name", "phone",  )


class StudentForm(forms.ModelForm):
    class Meta:
        model = student
        fields = ("standard", )


class TeacherForm(forms.ModelForm):
    class Meta:
        model = teacher
        fields = ("subject",  )


class DoubtForm(forms.ModelForm):
    class Meta:
        model = doubt
        fields = ("subject", "question", "language" ,  )


