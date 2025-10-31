from django.urls import path 
from student.views import student_view , student_view1 , student_view2 , student_view3 , student_above_score , course_student  , student_courses , change_task
from student.class_view import AllStudentView 

app_name = "student"

urlpatterns = [
    path ("all/" , student_view) ,
    path ("new/" , student_view1) ,
    path ("course/" ,student_view2) , 
    path ("all_student/" ,student_view3 , name="student_list") , 
    path ("studente_score/<int:sco_id>/" ,student_above_score) ,   #1
    path ("course_student/<int:course_id>/" ,course_student ) ,    #2
    path ("student_courses/<int:stu_id>/" , student_courses ) ,    #3
    path ("change_task/<int:task_id>/" , change_task ) ,           #4
    path ("all_student_new/" , AllStudentView.as_view(), name= "student_list_new") 
]
  
   