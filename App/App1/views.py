from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.views.decorators.csrf import csrf_exempt
from .forms import signupForm
from .admin import UserAdmin

# Create your views here.
def home(request):
    return render(request,'home.html')

@csrf_exempt
def signup(request):
    if request.method == 'POST':
        fm = signupForm(request.POST)
        #username = request.POST['username']
        #password = request.POST['password']
        #data = User.objects.create_user(username=username, password=password)
        #data.save()
        if fm.is_valid():
            fm.save()

            return redirect('home')
    else:
        fm = signupForm()
    return render(request,'Signup.html',{'form':fm})

 # add to imports
from django.contrib.auth import login, authenticate  # add to imports
@csrf_exempt
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user=signupForm(request.POST)
        if user is not None:
            #login(request, user)
            return redirect('home')
    return render(request,'login.html')



