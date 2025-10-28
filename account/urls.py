from django.urls import path 
from account.views import RegisterView

app_name = "account" 

urlpatterns = [
    path ("user-register/", RegisterView.as_view(), name= "user-register") ,
]
