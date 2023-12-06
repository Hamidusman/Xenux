from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')


def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        if email is not None:
            user = User.authenticate(email=email, password=password)
            auth.login(request, user)
            return redirect('')
        else:
            messages.info('Incorrect email/password')
            return redirect('login')
            
    return render(request, 'login.html')

def register(request):
    return render(request, 'reg.html')