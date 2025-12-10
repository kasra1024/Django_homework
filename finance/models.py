from django.db import models

# Create your models here.

class Category (models.Model) : 
    name = models.CharField(max_length=128) 
    def __str__(self):
        return self.name

# هر درامد فقط توی ی دسته جا میشه 
class Income(models.Model) : 
    amount = models.IntegerField() 
    descriptions = models.CharField(max_length=256 , blank=True , null=True) 
    date = models.DateField(auto_now_add=True) 
    category = models.ForeignKey(Category , on_delete= models.SET_NULL , null=True , blank=True , related_name="income") 
    def __str__(self):
        return f"{self.amount} درامد"

# هر هزیت=نه هم توی دسته جا میشه 
class Expense (models.Model) : 
    amount = models.IntegerField() 
    descriptions = models.CharField(max_length=256 , blank=True , null=True) 
    date = models.DateField(auto_now_add=True) 
    category = models.ForeignKey(Category , on_delete= models.SET_NULL , null=True , blank=True , related_name="expense") 
    def __str__(self):
        return f"{self.amount} هزینه"

    