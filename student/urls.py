from django.urls import path 
from student.views import student_view , student_view2 , student_view3 , AddCourse 
from student.class_view import AllStudentView 
from student.class_view import AllTeacher , AllStudentView1 , CourseListView

app_name = "student" 

urlpatterns = [
    path ("all/" , student_view) ,
    path ("course/" ,student_view2) , 
    path ("all_student/" ,student_view3 , name="student_list") , 
    path ("all_student_new/" , AllStudentView.as_view(), name= "student_list_new") ,
    path ("course_student_form/" , AddCourse, name="course_add"),
    path ("all_teacher/" , AllTeacher.as_view()),                                            #1
    path ('all_student_view1' , AllStudentView1.as_view()),                                  #2
    path ('CourseListView' , CourseListView.as_view() , name='course_detail'),               #4

]
  
    