
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login
from django.shortcuts import render, redirect
from .models import Education, Experience, Skill, Profile
from django.contrib import messages
# Create your views here.

def index(request):  
    return render(request, 'index.html')

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(request, username=email, password=password)

        if user is not None:
            auth_login(request, user)
            messages.success(request, 'Login successful')
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
                user.firstname = firstname
                user.middlename = middlename
                user.surname = surname
                user.save()

                # Pass the email to the template

                return redirect('login')
        else:
            messages.info(request, "Passwords don't match")
            return redirect('reg')
    else:
        # Handle GET requests for the registration page
        return render(request, 'reg.html')  # Assuming 'registration.html' is your registration template

def profie(request):
    user_info = Profile.objects.get(owner=request.user)
    if request.method = 'POST':
        age = requests.POST['age']
        address = request.POST['address']
        occupation = request.POST['occupation']
        phone_number = request.POST['phone_number']
        about = request.POST['about']

        user_info.age = age
        user_info.address = address
        user_info.occupation = occupation
        user_info.phone_number = phone_number
        user_info.about = about
        user_info.save()
        return redirect('/')
    return render(request, 'profile.html')


def education(request):
    education = Education.objects.filter(owner=request.user)
    
    if request.method == 'POST':
        certification = request.POST['degree']
        institution = request.POST['institution']
        duration = request.POST['duration']
        description = request.POST['description']

        # Use try-except block to catch any potential exceptions during object creation
        try:
            Education.objects.create(owner=request.user, certification=certification, institution=institution, duration=duration, description=description)
            messages.info(request, 'Education record saved!')  # Pass the request object to the messages.info function
        except Exception as e:
            messages.error(request, f'Error saving education record: {e}')  # Handle any exceptions and display an error message

    return render(request, 'education.html', {'education': education})

def experience(request):
    experience = Experience.objects.filter(owner = request.user)
    if request.method == 'POST':
        position = request.POST['position']
        organization = request.POST['organization']
        duration = request.POST['duration']
        description = request.POST['description']

        try:
            Experience.objects.create(owner=request.user,
                                      position=position,
                                      organization=organization,
                                      duration=duration,
                                      description=description)
            messages.info(request, 'Experience saved!')
        except Exception as e:
            messages.info(request, f'request failed {e}')
    context = {'experience': experience}
    return render(request, 'experience.html', context)


def skills(request):
    skills = Skill.objects.filter(owner= request.user)
    if request.method == 'POST':
        skill1 = request.POST['skill1']
        skill2 = request.POST['skill2']
        skill3 = request.POST['skill3']

        try:
            Skill.objects.create(owner=request.user, skill1=skill1, skill2=skill2, skill3=skill3)
            messages.info(request, 'Skills updated successfully')

        except Exception as e:
            messages.info(request, f'an error occured, {e}')


    return render(request, 'skills.html')


def resume(request):
    experience = Experience.objects.filter(owner=request.user)
    education = Education.objects.filter(owner = request.user)
    skills = Skill.objects.filter(owner=request.user)
    firstname = request.user.first_name
    context = {
    'experience': experience,
    'education': education,
    'skills': skills,
    'user': request.user,  # Include the user variable in the context
}
    return render(request, 'resume.html', context)