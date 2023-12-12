from django.shortcuts import render, HttpResponseRedirect
from .models import Blog
from django.contrib import messages
from .forms import blog_form, signup_form
from django.contrib.auth import get_user ,authenticate, login, logout
# Create your views here.
def Home(request):
    os = Blog.objects.all()
    uname = request.user
    return render(request, 'main_page.html', {'data':os, 'uname':uname})

def Creation(request):
    if request.user.is_authenticated:
        if request.method == "GET":
            uname = request.user
            fm = blog_form(initial={'user':uname})
            fm = blog_form(request.GET) 
            if fm.is_valid():
                fm.save()
                messages.success(request, "Posted successfully...")
                return HttpResponseRedirect('/home/')
        else:
            fm = blog_form()
            uname = request.user
        return render(request, 'create.html', {'form':fm, 'uname':uname})
    
    else:
        return HttpResponseRedirect('/login/')

def my_page(request):
    if request.user.is_authenticated:
        a = Blog.objects.filter(user=request.user)
        print(a)
        user = request.user
        return render(request, 'my_page.html', {'data':a, 'uname':user})
    else:
        return HttpResponseRedirect('/login/')


def Signup(request):
    if request.method == "POST":
        sf = signup_form(request.POST)
        if sf.is_valid():
            sf.save()
            sf = signup_form()
    else:
        sf = signup_form()
    return render(request, "signup.html", {'form':sf})

def Login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/home/')
    return render(request, 'login.html')

def Logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')


