from rest_framework.views import APIView
from student.models import Student
from rest_framework.response import Response

class AllStudentApiView(APIView) : 
    def get (self , request) : 
        students_id = Student.objects.all().values_list("fullname" , flat=True)
        students_dict = {"id" : students_id} 
        return Response (students_dict)

    def post (self , request) : 
        Student.objects.create(

        )
        return Response({"message" : "ok"})
    

    def put (self , request , pk) : 
        print (pk)
        print (request.data)
        return Response({"message" : "ok by"})


    def delete (self , request , pk ) : 
        print (pk)
        print (request)
        return Response({"message" : "ok delete"})

