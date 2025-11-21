from django.urls import path 
from student.views import *
from student.api import *
from student.class_view import *

app_name = "student" 

urlpatterns = [ 
    path ("all/" , student_view) ,
    path ("course/" ,student_view2) , 
    path ("all_student/" ,student_view3 , name="student_list") , 
    path ("all_student_new/" , AllStudentView.as_view(), name= "student_list_new") ,
    path ("course_student_form/" , AddCourse, name="course_add"),
    path ("all_teacher/" , AllTeacher.as_view()),                                             #1
    path ('all_student_view1/' , AllStudentView1.as_view()),                                  #2
    path ('CourseListView/' , CourseListView.as_view() , name='course_detail'),               #4
# -------------------------------------------------------------------------------------------------------------------------
    path("listcourse/" , ListCourse.as_view()) ,
    path("coursepk/" , CoursePk.as_view()) ,
    # path("CourseCreateView/" , CourseCreateView.as_view()),
    path ("TaskListView/" , TaskListView.as_view()) ,
# ------------------------------------------------------------------------------------------------------------------------------

    # api urls
    path ('api/all_students/' , AllStudentApiView.as_view()) , 
    path ('api/all_students/<int:pk>/' , AllStudentApiView.as_view()) ,
    # ---------------------------------------------------------------------
    # practice
    path ('api/ListStudent/' , ListStudent.as_view()) ,
    path ('api/ListStudentid/<int:pk>/' , ListStudent.as_view()) , 
    path ('aip/AllCourseApi/' , AllCourseApi.as_view()) , 
    path ('api/AllCourseApiid/<int:pk>/' , AllCourseApi.as_view()) , 
    path ('api/ProfileApi/<int:pk>/' , ProfileApi.as_view()) , 




]

