from rest_framework import serializers
from student.models import Course , Student , Teacher , profile


# class StudentSerializer(serializers.Serializer) : 
#     fullname = serializers.CharField() 
#     score = serializers.IntegerField() 
class StudentSerializer(serializers.ModelSerializer): 
    class Meta : 
        model = Student
        fields = ["fullname" , "score"]



# (3) , (4)
class TeacherApiSerializer(serializers.ModelSerializer) : 
    # courses =serializers.PrimaryKeyRelatedField(many = True , read_only = True)
    courses = serializers.SerializerMethodField()
    class Meta : 
        model = Teacher
        fields = ["fullname" , "score" , "courses"]

    def get_courses (sefl , obj) : 
        return obj.courses.values()



class CourseSerializerzer (serializers.ModelSerializer) : 
    # students = serializers.ListField(write_only = True , required = False)
    # students = StudentSerializer(many=True)
    students = serializers.SerializerMethodField()
    teachers = TeacherApiSerializer(read_only = True)
    class Meta : 
        model = Course
        fields = "__all__"
    def get_students(self , obj) : 
        result = obj.students.values("fullname" , "score")
        return result




# (1) , (4)
class StudentApiSerializer(serializers.ModelSerializer) : 
    class Meta : 
        model = Student 
        fields = ["fullname" , "score"]


# (2) 
class CoursesApiSerializer(serializers.ModelSerializer) : 
    class Meta : 
        model = Course
        fields = "__all__"


# (4) 
class ProfileApiSerializer(serializers.ModelSerializer): 
     class Meta: 
         model = profile
         fields = "__all__"
    