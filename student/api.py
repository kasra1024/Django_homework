from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet , ModelViewSet
from student.models import Student , Teacher
from student.models import Course
from student.models import profile
from rest_framework.response import Response
from rest_framework import status
from django.core.exceptions import ObjectDoesNotExist
from student.serializers import *
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated 
from student.permissions import *
# from rest_framework.pagination import PageNumberPagination
from student.paginations import NewPagination 
from django_filters.rest_framework import DjangoFilterBackend
from student.filters import CourseFilter
from django.core.management import call_command
class AllStudentApiView(APIView) : 
    def get (self , request , pk) : 
        if pk : 
            students_id = Student.objects.get(id = pk)
            return Response({"name" : students_id.fullname , "score" :students_id.score})
        else : 
            students_name = Student.objects.all().values("fullname" , flat = True)
            student_dict = {"student" : students_name}
            return Response (student_dict)
    


    def post (self , request) : 
       data = request.data 
       srz_data = StudentSerializer(data = data)
       if srz_data.is_valid () : 
           Student.objects.create(fullname = data["fullname"] , score = data["score"])
        #    srz_data.save()
           return Response ({"message" : "ok my dear"} , status=status.HTTP_201_CREATED )
       else : 
            return Response ({"message" : "validations error"} , status=status.HTTP_400_BAD_REQUEST)

    
    


    def put (self , request , pk) : 
        print (pk)
        print (request.data)
        return Response({"message" : "ok by"})






    def delete (self , request , pk ) : 
        print (pk)
        print (request)
        return Response({"message" : "ok delete"})
    
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------
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
    def get (self , request , pk=None) : 
        if pk : 
            course = Course.objects.get(id = pk)
            return Response ({
                "title" : course.title ,
                "description" : course.description
            })
        else : 
            allcourse = Course.objects.all().values_list("title" , flat=True)
            courses = {"allcourse" : allcourse}
            return Response(courses)
#(3) 
class EnrollApiView (APIView) : 
    def post (self , request) : 
        data = request.data
        st_id = data["student_id"]
        cr_id = data["course_id"]
        try : 
            student1 = Student.objects.get(id = st_id)
            course1 = Course.objects.get(id = cr_id)
            student1.courses.add(course1)
            if course1 in student1.courses.all() : 
                return Response ({"message" : "student is befor add"} , status=status.HTTP_400_BAD_REQUEST) 
        except ObjectDoesNotExist : 
            return Response ({"message" : "error Does Not Exist"} , status=status.HTTP_404_NOT_FOUND) 
        return Response ({"message" : "course add"} , status=status.HTTP_200_OK) 
# (4) 
class ProfileApi (APIView) : 
    def get (self , request , pk) : 
        profiles = profile.objects.filter(id = pk).values("id" , "bio" , "avatar" , "phone_number" , "img" , "file" , "user")
        profile1 = {"profiles" : profiles}
        return Response (profile1)
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------
# viewset
# class CourseViewSet(ViewSet) : 
#     def retrieve (self , request , pk) : 
#         srz_data = CourseSerializerzer(instance = Course.objects.get(id = pk))
#         return Response(srz_data.data)
    

#     def list (self , request) : 
#         srz_data = CourseSerializerzer(instance = Course.objects.all() , many=True)
#         return Response(srz_data.data)



# --------------------------------------------------------------------------------------------------------------------------------------------------------------------
# modelviewset 
class CourseViewSet(ModelViewSet) : 
    queryset = Course.objects.all() 
    serializer_class = CourseSerializerzer 
    permission_classes = [IsAuthenticated , ModifyCourse]
    pagination_class = NewPagination 
    # authentication_classes = []    #خودمون دستیم میایم میزاریم ک این کورس نیازی نداره به اینکه یوزر لاگین کرده باشه 
    filter_backends = [DjangoFilterBackend]
    # filterset_fields = ["active" , "code"]
    filterset_class = CourseFilter

    def get_permissions(self):
        if self.request.method in ["POST" , "PUT" , "PATCH" , "DELETE"] : 
            return [IsAuthenticated() , ActiveCourse(), IsTeacher()]
        else : 
            return [IsAuthenticated() , ActiveCourse()]
        # return super().get_permissions()


    # def retrieve (self , request , pk) : 
    #     srz_data = self.serializer_class(instance = self.queryset.get(id = pk))
    #     data = srz_data.data 
    #     teacher = Teacher.objects.get(id =data["teacher"] )
    #     data["teacher"] = {"fullname" : teacher.fullname , "score" : teacher.score}
    #     return Response(data)
    
    # def list (self , request) : 
    #     srz_data = CourseSerializerzer(instance = self.queryset , many=True)
    #     call_command("test1" , 12)
    #     return Response(srz_data.data)



    # def create (self , request) : 
    #     srz_data = CourseSerializerzer(data = request.data)
    #     if srz_data.is_valid() : 
    #         srz_data.save()
    #         return Response ("ok")
    #     return Response (srz_data.errors)


    @action(detail=False) 
    def is_active_list(self , request) : 
        q = Course.objects.filter(is_active = True)
        srz_data = self.serializer_class(instance = q , many=True)
        return Response (srz_data.data)
# -----------------------------------------------------
# (1)
class StudentModelViewSet(ModelViewSet) : 
    queryset = Student.objects.all()
    serializer_class = StudentApiSerializer
# -----------------------------------------------------
# (2) 
class CourseModelViewSet(ModelViewSet) : 
    queryset = Course.objects.all() 
    serializer_class = CoursesApiSerializer
# ------------------------------------------------------
# (3) 
class TeacherModelViewSet(ModelViewSet) : 
    queryset = Teacher.objects.all()
    serializer_class = TeacherApiSerializer
# ------------------------------------------------------
# (4)
class StudentModelViewSet(ModelViewSet) : 
    queryset = Student.objects.all()
    serializer_class = StudentApiSerializer

    # def create (self,request) : 
    #     srz_data = StudentApiSerializer(data = request.data)
    #     if srz_data.is_valid() : 
    #         srz_data.save()
    #         return Response("ok" , status=status.HTTP_201_CREATED)
    #     return Response ("error" , status=status.HTTP_400_BAD_REQUEST)
#-------------------------------------------------------------------------------------
# (4)
# class TeacherModelViewSet(ModelViewSet) : 
#     queryset = Teacher.objects.all()
#     serializer_class = TeacherApiSerializer

    # def create (self,request) : 
    #     srz_data = TeacherApiSerializer(data = request.data)
    #     if srz_data.is_valid() : 
    #         srz_data.save()
    #         return Response("ok" , status=status.HTTP_201_CREATED)
    #     return Response ("error" , status=status.HTTP_400_BAD_REQUEST)
# ---------------------------------------------------------------------------------------
# (5)
class ProfileModelViewSet(ModelViewSet) : 
    queryset = profile.objects.all() 
    serializer_class = ProfileApiSerializer