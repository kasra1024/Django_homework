from django.shortcuts import render , redirect
from django.views import View
from django.contrib.auth.models import User
# Create your views here.
from account.forms import UserRegiseterForm , UserLoginForm
from django.contrib.auth import authenticate , login , logout
from student.models import profile
from django.shortcuts import get_object_or_404
from django.contrib import messages

# --------------------------------------------------------------------------------
# authenticated ساخت هویت یا یوزر 

class RegisterView(View) :
    form = UserRegiseterForm()
    template = "account/regiseter.html"

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
# ---------------------------------------------------------------------------------
# login

class LoginUserView(View) : 
    form = UserLoginForm ()
    html = 'account/login.html'

    def get (self , request) :
        return render (request , self.html , {'form' : self.form})
    

    def post (self , request) : 
        form = UserLoginForm(request.POST) 
        user = authenticate(username = request.POST['username'] , password =request.POST['password'])
        if user and user.is_authenticated : 
            login(request , user)
            # messages.add_message(request , messages.SUCCESS , 'login successfuly')
            return redirect ('account:user_profile')
        return render(request , self.html , {"form" : self.form , 'message' : "بوزرنیم و پسورد اشتباه طناز"})
# ------------------------------------------------------------------------------------------------------------------------------------------
# logout

class LogoutView (View) : 
    def get (self , request) : 
        if request.user.is_authenticated : 
            logout(request)
        return redirect ("account:user_login")
    
# -----------------------------------------------------------------------------------------------------------------------------------------------

# delete account

class DeleteAccountView(View) : 
    def get (self , request) : 
        if request.user.is_authenticated : 
            try : 
                user = User.objects.get(id=request.user.id)                                                                             
                user.delete()
                return redirect("todo:home")
            except : 
                return redirect("student:course_add")
            


class ProfileView(View) : 
    html="account/profile.html"
    def get (self , request) : 
        if request.user.is_authenticated : 
            # Profile = profile.objects.get(id=request.user.id)
            Profile = get_object_or_404(profile , user_id=request.user.id)
            if Profile.is_student : 
                extinded_data = profile.student
            else : 
                 extinded_data = profile.teacher
            
            return render(request , self.html , {'Profile' : Profile , 'extended_data' : extinded_data , 'message' : "با موفقیت وارد شدید"})
        else : 
            return redirect ('account:user_login')