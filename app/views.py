from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password, check_password
from .models import RegisteredUsers
from django.contrib import messages


# show login page


def register_page(request):
    return render(request, "register.html")

@api_view(["POST"])
def register(request):

    username = request.data["username"]
    phone_number=request.data["phone_number"]
    email = request.data["email"]
    age = request.data["age"]
    address=request.data["address"]
    password = request.data["password"]
    confirm_password = request.data["confirm_password"] 

    if password != confirm_password:
            messages.error(request, "Passwords do not match")
            return render(request, "register.html")

    hashed_password = make_password(password)

    RegisteredUsers.objects.create(
        username=username,
        phone_number=phone_number,
        email=email,
        age=age,
        address=address,
        password=hashed_password,
        
    )

    messages.success(request, "User Registered Successfully!")
    
    return redirect("register")


def login_page(request):

    if request.method == "POST":
        phone_number = request.POST.get("phone_number")
        password = request.POST.get("password")

        try:
            user = RegisteredUsers.objects.get(phone_number=phone_number)

            if check_password(password, user.password):
                messages.success(request, "Login Successful")
                return redirect("dashboard")    

            else:
                messages.error(request, "Invalid Password")

        except RegisteredUsers.DoesNotExist:
            messages.error(request, "Phone_number does not exist")

    return render(request, "login.html")



def manager(request):
    pass