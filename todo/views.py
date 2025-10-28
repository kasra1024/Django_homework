from django.shortcuts import render
from django.http import HttpResponse 
# Create your views here.
from todo.models import task
from student.models import Student  , Course



# --------------------------------------------
def len2 (text) : 
    return len(text)
def home (request) :
    x = task.objects.all()
    titles = []
    for i in x : 

        z = len2 (i.title)
        titles.append(str(z))
    new =" ".join(titles)

    return HttpResponse (titles)  
# ---------------------------------------------


def home2 (request): 
    tasks =  list(task.objects.all())
    context = {'list_task' : tasks}
    return render (request , 'todo/new.html' , context)

# -------------------------------------------------------------------

def home3 (request): 
    Tasks = list( task.objects.all())
    titlesss = []
    for i in Tasks : 
        titlesss.append(i.title)

        context = {'task_titles' : titlesss}
    return render (request , 'todo/new.html' , context)


# ----------------------------------------------------------------
def home4 (request) : 
    return HttpResponse (""" 
                         <h1>hello</h1>
                         <p>fuck you</p>
                         """
                         )

# ---------------------------------------------------------------------
def task_student (request , st_id) : 
    student_obj = Student.objects.get(id=st_id)
    


    if student_obj.fullname == "ali" : 
        student_obj.fullname = "ksara" 
    elif student_obj.fullname == "ali" :
        student_obj.fullname = 'kasra'
    student_obj.save()





    task.objects.create(
        title = "new_task" , 
        done = False , 
        catgory = "sport" , 
        description = "desc new task " , 
        student = student_obj 
    )
    course = Course.objects.get(code =123)
    course.students.remove(student_obj)




    tasks_student = task.objects.filter(student_id = st_id)
    context = {"task": tasks_student}
    return render (request , 'todo/new.html' , context)
 

# ما میخایم هر بار ک ریکوس میزنیم بره تسک بسازه بعد ک ابجکت استیودنت ر ساختی حالا بیا همه ی تسک هاشو نشون بده 
# -------------------------------------------------------------------------------------------------------------------------------

