from django.db import models
from student.models import Student

# Create your models here.

class task (models.Model) :                                                                                                                                                                                                                                                                                                                                                                                                                                                                 
    title = models.CharField(max_length=256)
    done = models.BooleanField(default=False)
    catgory = models.CharField(max_length=64)
    description = models.TextField()
    student = models.ForeignKey (Student , on_delete=models.CASCADE ,related_name="task")
    # date = models.DateField()  
    def __str__(self):
        return self.title

class typecategory (models.Model) : 
    title = models.CharField(max_length=32)
    tasks = models.ManyToManyField(task) 
    def __str__(self):
        return self.title  