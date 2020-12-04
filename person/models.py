from django.db import models
from django.contrib.auth.models import User
from enum import Enum
import datetime


class Type(Enum):
    Student  = "Student"
    Teacher  = "Teacher"
    Admin    = "Admin"


class person(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    f_name = models.CharField(max_length=25)
    l_name = models.CharField(max_length=25, blank=True)
    phone = models.CharField(max_length=11)
    user_type = models.CharField(max_length=10, choices=[(tag.name, tag.value) for tag in Type],
                     default=Type.Student)
    #photo = models.FileField(upload_to='profile_pic/', blank=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.f_name



class teacher(models.Model):
    prsn = models.OneToOneField(person, on_delete=models.CASCADE)
    subject = models.CharField(max_length=20)
    verified = models.BooleanField(default=False)

    def __str__(self):
        return self.prsn.f_name



class student(models.Model):
    prsn = models.OneToOneField(person, on_delete=models.CASCADE)
    standard = models.CharField(max_length=5)
    #school_name = models.CharField(max_length=5)

    def __str__(self):
        return self.prsn.f_name



class doubt(models.Model):
    student = models.OneToOneField(person, on_delete=models.CASCADE)
    subject = models.CharField(max_length=20)
    teacher = models.CharField(max_length=20, blank=True )
    question = models.TextField(blank=True)
    answer   = models.TextField(default = "Unanswered" )
    language = models.CharField(max_length=10)
    is_answered = models.BooleanField(default=False)

    def __str__(self):
        return self.question


