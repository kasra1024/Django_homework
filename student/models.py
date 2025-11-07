from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Student(models.Model) : 
    username = models.CharField(max_length=54 , null=True , blank=True)
    fullname = models.CharField(max_length=64)
    username = models.CharField(max_length=64) 
    score = models.IntegerField(default=0)
    Profile = models.OneToOneField('profile' , related_name= 'student' , on_delete= models.CASCADE  , null=True , blank=True)
    
    def __str__(self):
        return self.fullname 
    

class Teacher (models.Model) : 
    fullname = models.CharField(max_length=64)
    score = models.IntegerField(default=0)
    Profile = models.OneToOneField ('profile' , related_name= 'teacher' , on_delete= models.CASCADE , null=True , blank=True)
    
 
class Course (models.Model) : 
    title = models.CharField(max_length=32) 
    code = models.IntegerField()
    decription = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    students = models.ManyToManyField(Student , related_name= "Course" , blank=True) 
    teachers = models.ForeignKey(Teacher , on_delete=models.CASCADE , blank=True , null=True, related_name='courses')
    active = models.BooleanField(default=True) 
    def __str__(self):
        return self.title
    


    
class profile (models.Model) : 
    bio = models.TextField() 
    avatar = models.ImageField(upload_to="images/%Y/%m/" , null=True)
    phone_number = models.CharField(max_length=13)
    img = models.ImageField(upload_to="images/%Y/%m/" , null=True , blank=True)
    file = models.FileField(upload_to="files/%Y/%m/" , null=True , blank=True)
    user = models.OneToOneField(User , related_name= 'student' , on_delete= models.CASCADE  , null=True , blank=True)
    is_student = models.BooleanField(default=True)
    def __str__(self):
        return self.bio
 

