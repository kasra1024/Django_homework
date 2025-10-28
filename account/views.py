from django.shortcuts import render , redirect
from django.views import View
from django.contrib.auth.models import User
# Create your views here.
from account.forms import UserRegiseterForm



class RegisterView(View) :
    form = UserRegiseterForm()
    template = "account/register.html"

    def get (self , request) : 
        return render(request , self.template , {"form": self.form})
        


    def post (self , request) : 
        st_form = UserRegiseterForm(request.POST)
        if st_form.is_valid() : 
            # new_user = st_form.save() 
            new_user = User.objects.create_user(
                username=request.POST["username"] , 
                email="" , 
                password= request.POST["password"]

            )
            if new_user : 
                return redirect ("todo:home")
        return render(request , self.template
                       , {"form": self.form , "message" : "username is valid" })