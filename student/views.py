from django.shortcuts import render , get_object_or_404

from student.models import Student

from student.models import Course

from todo.models import task


def student_view(request) : 
    all_student = Student.objects.filter(score__gt=15)
    create_student = Student.objects.create(fullname = "maka" , username = "maka" , score =  "19")

    context = {"students" : all_student ,
               "new_student" : create_student}
    html_file = "student/all_student.html"
    return render (request, html_file , context)


def student_view1 (request) : 
    create_student = Student.objects.create(fullname = "maka" , username = "maka" , score =  "19")
    context = {"new_student" : create_student}
    html_file = "student/all_student.html"
    return render (request, html_file , context)


# --------------------------------------------------------------------------------------------------------

def student_view2 (request) : 
    all_course = Course.objects.all() 
    context = {"all" : all_course}
    return render (request , "student/course.html" , context)
# -----------------------------------------------------------------------

def student_view3 (request) : 
    all_student = Student.objects.all()
    context = {"students" : all_student} 
    return render (request , "student/all_student.html" , context )
  

# -------------------------------------------------------------------------------------------------------




# (1)

def student_above_score (request , sco_id) : 
    student_above = Student.objects.filter(score__gt = sco_id)
    context = {"student_score" : student_above}
    return render (request , "student/student_score.html" , context) 






# -------------------------------------------------------------------------------------------------------



# (2)

def course_student (request , course_id) : 
    coursess = Course.objects.filter(id= course_id) 
    context = {"cors_st" : coursess}
    return render (request , "student/course_student.html" , context)





# ----------------------------------------------------------------------------------------------------------

# (3) 

def student_courses (request , stu_id) : 
    student = Student.objects.filter(id = stu_id)
    context = {"students" : student}
    return render (request , "student/student_course.html" , context)





# ---------------------------------------------------------------------------------------------------------------

# (4) 

def change_task (request , task_id) : 
    task_obj = task.objects.get(id = task_id)
    task.done = not task.done
    task.save() 
    context = {"Task" : task_obj}
    return render (request , 'student/change_task.html' ,context )
