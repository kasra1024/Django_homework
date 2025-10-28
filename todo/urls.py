from django.urls import path 
from todo.views import *

app_name ="todo"


urlpatterns = [
    path ("home/" , home , name="home")  ,
    path ("home2/" ,home2) ,
    path ("home3/" ,home3) ,
    path ("home4/" ,home4) ,
    path ("home5/<int:st_id>/" , task_student) ,
]    