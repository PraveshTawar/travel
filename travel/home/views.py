from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
@login_required(login_url='/login/') # agar login nhi h or direct home pr jaye to ,it redirect to login page(login_required means without login you can not enter in home page)
def Home(request):
    return render(request,"travel.html")

def signup(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        Username = request.POST.get('Username')
        password1 = request.POST.get('Password1')
        password2 = request.POST.get('Password2')

        if password1!=password2:
            messages.info(request,"Password not matched")
            return redirect(signup)
        else:
            messages.info(request,"User has been Created")
            
            myuser = User.objects.create_user(username=Username,password=password1,first_name=first_name,last_name=last_name)
            # it create the user 
            myuser.save()
        
    return render(request,"Signup.html")

def login_page(request):
    if request.method=="POST":
        username = request.POST.get('Username')
        password = request.POST.get('Password1')
        user = authenticate(request,username=username,password=password) #it match the username and password stored in Admin database
        if user is not None: #means user is present in Admin database 
            login(request,user)
            return redirect(Home)
        else:
            messages.info(request,"Username and Password is wrong!")


    return render(request,"login.html")

def logout_page(request):
    logout(request)
    return redirect(login_page)

