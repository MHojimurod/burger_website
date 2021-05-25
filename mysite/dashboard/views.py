from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .services import *
from burger.models import *
from burger.forms import *



def login_required_decorator(f):
    return login_required(f, login_url="login")


@login_required_decorator
def dashboard_page(request):
    return render(request, 'dashboard/index.html')


def dashboard_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
    return render(request, 'dashboard/login.html')


def dashboard_logout(request):
    logout(request)
    return redirect('login')

def header(request):
    header_blog = get_header_info()
    ctx = {
        'header':header_blog
    }
    return render(request, 'dashboard/header/list.html',ctx)

def ourrecipes(request):
    our_recipes = get_ourrecipes()
    ctx = {
        'recipes':our_recipes
    }
    return render(request, 'dashboard/recipe/list.html',ctx)

def aboutourfoods(request):
    our_foods = get_ourfood()
    ctx = {
        'foods':our_foods
    }
    return render(request, 'dashboard/food/list.html',ctx)

def add_about_food(request):
    model = AboutOurFood()
    form = AboutOurFoodForm(request.POST, request.FILES, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('AboutOurFood')
        else:
            print(form.errors)
    ctx = {
        "form": form,
    }
    return render(request, 'dashboard/food/form.html', ctx)

def edit_about_food(request, pk):
    model = AboutOurFood.objects.get(id=pk)
    form = AboutOurFoodForm(request.POST or None, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('AboutOurFood')
        else:
            print(form.errors)
    ctx = {
        'form': form
    }
    return render(request, 'dashboard/food/form.html', ctx)

def delete_about_food(request, pk):
    model = AboutOurFood.objects.get(id=pk)
    model.delete()
    return redirect('AboutOurFood')


def ourblogs(request):
    our_blog = get_ourblog()
    ctx = {
        'blog':our_blog
    }
    return render(request, 'dashboard/blog/list.html',ctx)

def add_blog(request):
    model = OurBlog()
    form = OurblogForm(request.POST, request.FILES, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('OurBlog')
        else:
            print(form.errors)
    ctx = {
        "form": form,
    }
    return render(request, 'dashboard/blog/form.html', ctx)

def edit_blog(request, pk):
    model = OurBlog.objects.get(id=pk)
    form = OurblogForm(request.POST or None, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('OurBlog')
        else:
            print(form.errors)
    ctx = {
        'form': form
    }
    return render(request, 'dashboard/blog/form.html', ctx)

def delete_blog(request, pk):
    model = OurBlog.objects.get(id=pk)
    model.delete()
    return redirect('OurBlog')


def clients(request):
    our_clients = get_clients()
    ctx = {

        'clients':our_clients
    }
    return render(request, 'dashboard/client/list.html',ctx)


def questions(request):
    questions = get_questions()
    ctx = {

        'questions': questions
    }
    return render(request, 'dashboard/blog/list.html', ctx)

def register(request):
    register = get_register()
    ctx = {

        'register': register
    }
    return render(request, 'dashboard/register/list.html', ctx)




def about(request):
    aboutourfood = get_ourfood()
    ctx = {
        'aboutourfood': aboutourfood,
    }
    return render(request, 'burger/main/about.html', ctx)
