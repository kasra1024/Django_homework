from django.contrib import admin

# Register your models here.

from student.models import Student , Course , profile , Teacher

class CourseAdmin (admin.ModelAdmin) : 
    list_display = ("title" , "code")



admin.site.register(Student) 
admin.site.register(Course , CourseAdmin) 
admin.site.register(profile)
admin.site.register(Teacher)
