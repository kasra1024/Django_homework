from django.shortcuts import render , redirect

from student.models import Student

from student.models import Course

from todo.models import task
from django.views import View

from student.forms import StudentForm , CourseStudentForm


# -------------------------------------------------------------------------------------------------------

# همه ی دانشجویان ب همراه دانشجو جدید
def student_view(request) : 
    all_student = Student.objects.filter(score__gt=15)
    create_student = Student.objects.create(fullname = "maka" , username = "maka" , score =  "19" , phone_number = '103941408')

    context = {"students" : all_student ,
               "new_student" : create_student}
    html_file = "student/all_student.html"
    return render (request, html_file , context)

# --------------------------------------------------------------------------------------------------------

# همه ی کورس ها ب همراه اسم دانشجویان
def student_view2 (request) : 
    all_course = Course.objects.all() 
    context = {"all" : all_course}
    return render (request , "student/course.html" , context)

# -----------------------------------------------------------------------------------------------------------

# ساخت دانشجو از طریق سایت ن پنل ادمین
def student_view3 (request) : 
    form = StudentForm() 
    if request.method == "GET" : 
        all_student = Student.objects.all()
        context = {"students" : all_student , "form" : form} 
        return render (request , "student/all_student.html" , context )
    elif request.method == "POST" : 
        d = StudentForm(request.POST)
        if d.is_valid():
            save_obj = d.save()
        # data = request.POST
        # fullname1 = data["fullname"]
        # username1 = data["username"]
        # phone1 = data["phone_number"]
        # student_obj = Student.objects.create(fullname="fullname1" , username="username1" , phone_number=phone1 , score=0)
            if save_obj :
                return redirect("todo:home")
        return render (request ,"student/all_student.html" , {"form" : form})
    




# ----------------------------------------------------------------------------------------------------------------
# # (1)
# def student_above_score (request , sco_id) : 
#     student_above = Student.objects.filter(score__gt = sco_id)
#     context = {"student_score" : student_above}
#     return render (request , "student/student_score.html" , context) 
# # ---------------------------------------------------------------------------------------------------------------
# # (2)
# def course_student (request , course_id) : 
#     coursess = Course.objects.filter(id= course_id) 
#     context = {"cors_st" : coursess}
#     return render (request , "student/course_student.html" , context)
# # ---------------------------------------------------------------------------------------------------------------
# # (3) 
# def student_courses (request , stu_id) : 
#     student = Student.objects.filter(id = stu_id)
#     context = {"students" : student}
#     return render (request , "student/student_course.html" , context)
# # ----------------------------------------------------------------------------------------------------------------
# # (4) 
# def change_task (request , task_id) : 
#     task_obj = task.objects.get(id = task_id)
#     task.done = not task.done
#     task.save()  
#     context = {"Task" : task_obj}
#     return render (request , 'student/change_task.html' ,context )
# -------------------------------------------------------------------------------------------------------------------

def AddCourse (request) : 
    
    template = "student/add_course.html"
    if request.method == "GET" :
        if request.user.is_authenticated: 
            form = CourseStudentForm()
            all_course = Course.objects.all() 
            return render (request , template , {"form" : form , "courses" : all_course}) 
    
    elif request.method == "POST" : 
        co_form = CourseStudentForm(request.POST)
        if co_form.is_valid () : 
            co_form.save() 
            return redirect ("account: user_register")
        else : 
            all_course = Course.objects.all() 
    return render (request , template , {"form" : form ,"courses" : all_course, "message" : "input is valid!!"}) 
# ----------------------------------------------------------------------------------------------------------------------



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
# -----------------------------------------
