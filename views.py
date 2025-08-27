from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
import time
# Create your views here.
from .models import Employee

def main(request):
      return render(request,'ems1/login.html')
      

def home(request):
      return render(request,'ems1/Signin.html',
)


def Signin(request):
 if request.method=="POST":
        first_name=request.POST["first_name"]
        last_name=request.POST["last_name"]
        date_joined=request.POST["date_joined"]
        email=request.POST["email"]
        username=request.POST["username"]
        password=request.POST["password"]
        user=User.objects.create_user(first_name=first_name,last_name=last_name,email=email,date_joined=date_joined,username=username,password=password)
        user.save()
        
        return render(request,"ems1/signin.html",{
            "user":user
        })
 else:
      print("error")
      return render(request,"ems1/mainpage.html")


def login_view(request):
 if request.method=="POST":
          username=request.POST["username"]
          password=request.POST["password"]
          user = authenticate(request,username=username,password=password)
          if user:
                login(request,user)
                return redirect("Employee_table")  
          else:
                print("try again")
                return render(request,"ems1/login.html")
 return render(request,"ems1/login.html",{"error":"invalid credetial"})


def logout(request):
      return rediect(request,"ems1/home.html")       

def Employee_table(request):
      employ_details=User.objects.all()
      return render(request,"ems1/employee.html",{
            "employee_details":employ_details
      })     

def update_details(request):
      return render(request,"ems1/update.html")

def Update(request, id):
   update = get_object_or_404(User, id=id)
   if request.method == "POST":
        UpdateEmail = request.POST.get("UpdateEmail")

        if UpdateEmail:
            update.email = UpdateEmail
            update.save()
            return HttpResponse("<h2>Updated Successfully</h2>")
        return render(request, "ems1/update.html", {"user": update})


def Delete(request,id):
      user = get_object_or_404(User, id=id)
      user.delete()
      time.sleep(1)
      return redirect("Employee_table")
