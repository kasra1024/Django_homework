from django.urls import path 
from account.views import RegisterView , LoginUserView , LogoutView , DeleteAccountView , ProfileView

app_name = "account" 

urlpatterns = [
    path ("user_register/" , RegisterView.as_view() , name="user_register") ,
    path ("user_login/" , LoginUserView.as_view() , name= "user_login") ,
    path ("user_logout/" , LogoutView.as_view() , name= "user_logout") ,
    path ("user_delete/" , DeleteAccountView.as_view() , name= "user_delete") ,
    path ("user_profile/" , ProfileView.as_view() , name= "user_profile") ,
]
