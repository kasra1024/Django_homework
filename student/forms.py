from django.forms import ModelForm 
from student.models import Student , Course , Teacher

class StudentForm(ModelForm) :
    class Meta : 
        model = Student
        fields = ["fullname"]


 


class CourseStudentForm (ModelForm) : 
    class Meta : 
        model = Course
        fields = ['title' , 'code' , 'decription' , 'start_date' , 'end_date']


