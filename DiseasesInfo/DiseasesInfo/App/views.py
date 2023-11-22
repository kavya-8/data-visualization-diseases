
#from django.http import HttpResponse
from django.shortcuts import render, redirect
#from django.contrib.auth.models import User, auth
from django.views.decorators.csrf import csrf_exempt
from .forms import signupForm
from .models import Diseases
#from .admin import UserAdmin

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


@csrf_exempt
def search(request):
    if request.method=="POST":
        searched=request.POST['searched']
        post = Diseases.objects.filter(Disease_Name__contains=searched)
        return render(request,'search.html',{'searched':searched,'post':post})
    else:
        return render(request, 'search.html', {})

def dashboard(request):
    return render(request, 'dashboard.html', )




def sample(request):
    post=Diseases.objects.all()
    return render(request, 'sample.html', {"post": post})

def dash(request):
    post=Diseases.objects.all()
    return render(request,'dash.html')

def search1(request):
    return render(request,'search1.html')

def search2(request):
    return render(request,'search2.html')

def search3(request):
    return render(request,'search3.html')

#def search4(request):
   # return render(request,'search4.html')