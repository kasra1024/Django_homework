from django.views import View
from student.models import *
from student.forms import *
from django.shortcuts import render , redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from todo.models import task

class AllStudentView (View) : 
    
    html_file = "student/all_student.html"

    form = StudentForm()
    def get (self , request) : 

        
        all_students = Student.objects.filter(fullname__exact="")
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
            




# ------------------------------------(1)
class AllTeacher (View) : 
    html = 'studen/teacher.html'
    def get (self , request) : 
        teachers = Teacher.objects.all() 
        return render (request , self.html , {'teachers' : teachers }) 
    
# -------------------------------------(2) 
class AllStudentView1(View) : 
    html = 'student/AllStudentView.html' 
    def get (self , request) : 
        stuendt = Student.objects.all() 
        return render (request , self.html , {"student" : stuendt})

# ----------------------------------------(4) 
class CourseListView(View) : 
    html = 'student/CourseListView.html' 
    def get (self , request) : 
        courses = Course.objects.filter(active=True).select_related('teacher')    #سرعت زیاد میکنه چون تیچر رو یک جا جوین میکنه
        return render(request ,self.html , {'courses' : courses} )
# -----------------------------------------

# تمرین ها سری اخر
class ListCourse (View) : 
    html = "student/ListCourse.html"

    def get (self , request) : 
        listcourse = Course.objects.all()
        return render (request , self.html , {"listcourse" : listcourse})
# ---------------------------------------
class CoursePk (View) : 
    html = "student/coursePk.html" 
    def get (self , request) : 
        listcourse = Course.objects.all()
        return render (request , self.html , {"listcourse" : listcourse})
# --------------------------------------------- 
# (3) 

# ////////////////////////////////////////////////
# 4

# class TaskListView(LoginRequiredMixin , View) :
#     html = "student/TaskListView.html" 
#     def get (self , request) : 
#         user = self.request.user 
#         if user == "student" : 
#             return task.objects.filter(student =user.student)
#         return task.objects.none()


class TaskListView(LoginRequiredMixin, View):

    def get(self, request):
        try:
            student = Student.objects.get(user=request.user)  # instance درست
            tasks = task.objects.filter(student=student)
        except Student.DoesNotExist:
            tasks = task.objects.none()

        context = {
            "tasks": tasks
        }
        return render(request, "task/TaskListView.html", context)