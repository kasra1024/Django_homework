from django.urls import path 
from todo.views import *

app_name ="todo"


urlpatterns = [
    path ("home/" ,home , name="home") ,
    path ("home1/<int:st_id>/" , task_student) ,
]   