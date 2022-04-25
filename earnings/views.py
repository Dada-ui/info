from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from earnings.models import *
from earnings.forms import *
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User


# Create your views here.

def cover(request):
    if not request.user.is_authenticated:
        return render(request,'cover.html')
    else:
        return redirect('home')
        

def loginview(request):
    if not request.user.is_authenticated:
        if request.method=='POST':
            username=request.POST['username']
            password=request.POST['password']
            user1=authenticate(request, username=username,password=password)
            if user1 is not None:
                login(request,user1)
                return redirect('home')
            else:
                messages.warning(request,'Invalid username or password')
                return render(request,'login.html')
        return render(request,'login.html')
    else:
        return redirect('home')


def logoutview(request):
    if request.user.is_authenticated:
        logout(request)
        return render(request,'logout.html')
    else:
        return redirect('lr')


def registerview(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            username = request.POST['username']
            email = request.POST['email']
            password = request.POST['password']
            user = User.objects.create_user(username,email,password)
            user.save()
            return redirect('login')
        return render(request,'register.html')
    else:
        return redirect('home')


def lr(request):
    if not request.user.is_authenticated:
        return render(request,'lr.html')
    else:
        return redirect('home')


@login_required(login_url='lr')
def user_profile(request):
    if not request.user.is_authenticated:
        return redirect('lr')
    else:
        return render(request,'user_profile.html')


@login_required(login_url='lr') 
def home(request):
    if request.user.is_authenticated: 
        task_claimed = list(Task_Model.objects.filter(user=request.user).values_list('app_id', flat=True))
        q = App_Model.objects.exclude(id__in=task_claimed)
    else:
        q = App_Model.objects.all()
    context = {"q": q}
    return render(request,'home.html',context)


@login_required(login_url='lr')
def add_apps(request):
    if request.method == 'POST':
        form = App_Form(request.POST, request.FILES) 
        if form.is_valid():
            form.save()
            messages.success(request,'New app added successfully..!')
            return redirect('home')
    else:
        form = App_Form()
    return render(request,'add_apps.html',{"form": form})


@login_required(login_url='lr') 
def app_details(request, pk):
    q = App_Model.objects.get(id=pk)
    if request.method == "POST":
        form = Task_Form(request.POST, request.FILES)
        if form.is_valid():
            t = form.save(commit=False)
            t.user = request.user
            t.app = q
            form.save()
            messages.success(request,'Task completed successfully..!')
            return redirect('home')
    else:
        form = Task_Form()
        d = {"form": form,"q": q}
    return render(request,'app_details.html',d)


@login_required(login_url='lr') 
def task(request):
    q = Task_Model.objects.filter(user=request.user)
    context = {'q':q}
    return render(request,'task.html',context)


@login_required(login_url='lr') 
def points(request):
    points = 0
    res = Task_Model.objects.filter(user=request.user)
    for i in res:
        points += i.app.point
    return render(request,'points.html',{"points": points})