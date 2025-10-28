from django.views import View
from student.models import *
from student.forms import StudentForm
from django.shortcuts import render , redirect


class AllStudentView (View) : 
    html_file = "student/all_student.html"

    form = StudentForm()
    def get (self , request) : 

        
        all_students = Student.objects.all()
        context = {"students" : all_students , "form" : self.form} 
        return render(request , self.html_file , context )
    
    def post (self , request) : 
        d = StudentForm(request.POST)
        if d.is_valid(): 
            save_obj = d.save()
            if save_obj : 
                return redirect ("todo:home")
            else : 
                return render (request , self.html_file , {"form" : self.form})