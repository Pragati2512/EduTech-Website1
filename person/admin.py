from django.contrib import admin
from .models import person, teacher, student

admin.site.register(person)
admin.site.register(teacher)
admin.site.register(student)
