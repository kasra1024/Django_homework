from rest_framework import serializers
from student.models import Course , Student , Teacher , profile


class StudentSerializer(serializers.Serializer) : 
    fullname = serializers.CharField() 
    score = serializers.IntegerField() 

# (2)
class CourseSerializerzer (serializers.ModelSerializer) : 
    # students = serializers.ListField(write_only = True , required = False)
    class Meta : 
        model = Course
        exclude = ["students"]


# (1) 
class StudentApiSerializer(serializers.ModelSerializer) : 
    class Meta : 
        model = Student 
        fields = ["fullname" , "score"]


# (2) 
class CoursesApiSerializer(serializers.ModelSerializer) : 
    class Meta : 
        model = Course
        fields = "__all__"



# (3)
class TeacherApiSerializer(serializers.ModelSerializer) : 
    class Meta : 
        model = Teacher
        fields = ["fullname" , "score"]