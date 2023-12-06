
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages
# Create your views here.

def index(request):
    return render(request, 'index.html')

def login_v(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)  # Corrected this line
            return redirect('/')
        else:
            messages.error(request, 'Incorrect email/password')
            return redirect('login')

    return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        middlename = request.POST['middlename']
        surname = request.POST['surname']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2: 
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email already exists')
                return redirect('reg')
            else:
                # Create and save the user
                user = User.objects.create_user(
                        username=email,
                        email=email,
                        password=password
                    )
                user.first_name = firstname
                user.middle_name = middlename
                user.last_name = surname
                user.save()
                return redirect('/')
        else:
            messages.info(request, "Passwords don't match")
            return redirect('reg')
    else:
        # Handle GET requests for the registration page
        return render(request, 'reg.html')  # Assuming 'registration.html' is your registration template

def experience(request):
    return render(request, 'work.html')