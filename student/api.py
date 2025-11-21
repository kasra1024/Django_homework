from rest_framework.views import APIView
from student.models import Student
from student.models import Course
from student.models import profile
from rest_framework.response import Response

class AllStudentApiView(APIView) : 
    def get (self , request) : 
        students_id = Student.objects.all().values_list("id" , flat=True)
        students_dict = {"id" : students_id} 
        return Response (students_dict)


    def post (self , request) : 
        print (request.data)
        return Response({"message" : "ok"})
    

    def put (self , request , pk) : 
        print (pk)
        print (request.data)
        return Response({"message" : "ok by"})


    def delete (self , request , pk ) : 
        print (pk)
        print (request)
        return Response({"message" : "ok delete"})
    
# ----------------------------------------------------------------------------------
# (1)
class ListStudent (APIView) : 
    def get (self , request) : 
        list_student = Student.objects.all().values_list("fullname", flat=True)
        student = {"student" : list_student}
        return Response (student)
    
    def get (self , request , pk) : 
        id_student = Student.objects.filter(id = pk ).values( "id" , "fullname" , "username" , "score")
        student1 = {"student_id" : id_student}
        return Response (student1) 


# (2)
class AllCourseApi (APIView) :  
    def get (self , request) : 
        allcourse = Course.objects.all().values_list("title" , flat=True)
        courses = {"allcourse" : allcourse}
        return Response(courses)
    
    def get (self , request , pk) : 
        title_course = Course.objects.filter(id = pk).values("id" , "title" , "code" , "decription" ,
                                                              "start_date" , "end_date" , "students" ,
                                                                "teachers" , "active")
        course1 = {"title_course" : title_course}
        return Response (course1)


#(3) 
class CourseViewApi (APIView) : 
    def post (self , request) : 
        pass 




# (4) 
class ProfileApi (APIView) : 
    def get (self , request , pk) : 
        profiles = profile.objects.filter(id = pk).values("id" , "bio" , "avatar" , "phone_number" , "img" , "file" , "user")
        profile1 = {"profiles" : profiles}
        return Response (profile1)


