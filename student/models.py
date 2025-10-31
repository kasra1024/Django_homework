from django.db import models

# Create your models here.

class Student(models.Model) : 
    fullname = models.CharField(max_length=64)
    username = models.CharField(max_length=64) 
    score = models.IntegerField(default=0)
    phone_number = models.IntegerField(max_length=13)
    img = models.ImageField(upload_to="images/%Y/%m/" , null=True)
    file = models.FileField(upload_to="files/%Y/%m/" , null=True)
    def __str__(self):
        return self.fullname 

class Course (models.Model) : 
    title = models.CharField(max_length=32) 
    code = models.IntegerField(max_length=32)
    decription = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    students = models.ManyToManyField(Student , related_name= "Course") 
    def __str__(self):
        return self.title
    

class profile (models.Model) : 
    bio = models.TextField() 
    avatar = models.CharField(max_length=128) 
    student = models.OneToOneField(Student , related_name= "profile" , on_delete= models.CASCADE)
    def __str__(self):
        return self.bio
 