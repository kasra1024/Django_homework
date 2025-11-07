from django.contrib import admin

# Register your models here.

from student.models import Student , Course , profile , Teacher

admin.site.register(Student) 
admin.site.register(Course) 
admin.site.register(profile)
admin.site.register(Teacher)