
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
#from django.contrib.auth.models import User, auth
from django.views.decorators.csrf import csrf_exempt
from .forms import signupForm
from .models import Diseases
from django.contrib import messages

#from .admin import UserAdmin

# Create your views here.
def home(request):
    return render(request,'home.html')

@csrf_exempt
def signup(request):
    fm=signupForm()
    if request.method == 'POST':
        fm = signupForm(request.POST)
        if fm.is_valid():
            fm.save()
            return redirect('home')
    return render(request,'Signup.html',{'form':fm})



@csrf_exempt
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user=authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username or password incorrect')
    return render(request,'login.html')

def logoutUser(request):
    return redirect('login')

@csrf_exempt
def search(request):
    if request.method=="POST":
        if 'searched' in request.POST:
            searched=request.POST['searched']
            post = Diseases.objects.filter(Disease_Name__contains=searched)
            return render(request,'search.html',{'searched':searched,'post':post})
    else:
        return render(request, 'search.html', {})

def dashboard(request):
    if request.method=="POST":
        searched=request.POST['searched']
        post = Diseases.objects.filter(Disease_Name__contains=searched)
        return render(request,'dashboard.html',{'searched':searched,'post':post})
    else:
        return render(request, 'dashboard.html', {})




def sample(request):
    post=Diseases.objects.all()
    return render(request, 'sample.html', {"post": post})

def dash(request):
    return render(request,'dash.html')

def search1(request):
    return render(request,'search1.html')

def search2(request):
    return render(request,'search2.html')

def search3(request):
    return render(request,'search3.html')

#def search4(request):
   # return render(request,'search4.html')

def dash2(request):
    return render(request,'dash2.html')


def dash4(request):
    return render(request,'dash4.html')

def dash5(request):
    return render(request,'dash5.html')

def dash6(request):
    return render(request,'dash6.html')