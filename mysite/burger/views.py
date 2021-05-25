from django.shortcuts import render,redirect
from dashboard.services import *
from .forms import *

def home(request):
    slide = get_header_info()
    ourrecipes = get_ourrecipes()
    aboutourfood = get_ourfood()
    ourblog = get_ourblog()
    client = get_clients()
    model = Questions()
    form = QuestionForm(request.POST, request.FILES, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            print(form.errors)
    ctx = {
        'ourrecipes':ourrecipes,
        'aboutourfood':aboutourfood,
        'ourblog':ourblog,
        'client':client,
        "form": form,
        "slide": slide,
    }
    return render(request, 'burger/main/index.html',ctx)

def about(request):
    aboutourfood = get_ourfood()
    ctx = {
        'aboutourfood': aboutourfood,
    }
    return render(request, 'burger/main/about.html',ctx)


def recipe(request):
    ourrecipes = get_ourrecipes()
    ctx = {
        'ourrecipes': ourrecipes,}

    return render(request, 'burger/main/recipe.html',ctx)


def blog(request):
    ourblog = get_ourblog()
    ctx = {
        'ourblog': ourblog,
    }
    return render(request, 'burger/main/blog.html',ctx)

def contact(request):
    return render(request, 'burger/main/contact.html')


def signup(request):
    model = Register()
    form = RegisterForm(request.POST, instance=model)
    if request.POST:
        password = request.POST.get("password")
        repeat = request.POST.get("re_pass")
        print(password,repeat)
        if password == repeat and form.is_valid():
            form.save()
            return redirect('home')
        else:
            form.errors()
    ctx = {
        'form': form
    }
    return render(request,'burger/signup.html',ctx)


def signin(request):
    client = get_register()
    model = Register()
    form = RegisterForm(request.POST, instance=model)
    for i in client:
        if request.POST:
            username = request.POST.get("username")
            password = request.POST.get("password")
            print(username,password)
            print(i['username'],'abc',i['password'])

            if username== i['username'] and password== i['password'] :
                print('hello')
                return redirect('home')
            else:
                forms.ValidationError('error')
    ctx = {
        'form': form
    }
    return render(request,'burger/signin.html',ctx)