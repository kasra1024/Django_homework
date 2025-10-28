from django.forms import ModelForm
from django.contrib.auth.models import User

class UserRegiseterForm (ModelForm) : 

    class Meta : 
        model = User
        fields = ["first_name" , "username" , "password"]
