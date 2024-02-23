from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.decorators import login_required


# Create your views here.

def signin(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username = username).exists():
            messages.error(request, 'Invalid username')
            return redirect('/signin/')
        
        user = authenticate(username = username, password = password)

        if user is None:
            messages.error(request, 'Invalid Password')
            return redirect('/signin/')
        
        else:
            login(request, user)
            return redirect('/dashboard/')


    return render(request, "signin.html")

# Register page
def signup(request): 

    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')
    
        user = User.objects.create(
            first_name = first_name,
            last_name = last_name,
            username = username
        )

        user.set_password(password)
        user.save()
        return redirect('/signin/')

    return render(request, 'signup.html')

def signout(request):

    logout(request)

    return redirect('/signin/')

@login_required(login_url = '/signin/')
def dashboard(request):
    return render(request, "dashboard.html")


def landing_page(request):
    return render(request, "landingpage.html") 

def profile_page(request):
    return render(request, "profile.html") 

def quicktest(request):
    return render(request, "quicktest.html")

def specialists(request):
    return render(request, "specialists.html")

def appointments(request):
    return render(request, "appointments.html")

def Analyze(request):
    return render(request, "Analyze.html")