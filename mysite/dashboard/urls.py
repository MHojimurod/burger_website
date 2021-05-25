from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard_page, name="dashboard"),
    path('login/', views.dashboard_login, name="login"),
    path('logout/', views.dashboard_logout, name="logout"),
    path('header/', views.header, name="header"),
    path('ourrecipes/', views.ourrecipes, name="OurRecipes"),
    path('aboutourfoods/', views.aboutourfoods, name="AboutOurFood"),
    path('ourblog/', views.ourblogs, name="OurBlog"),
    path('clients/', views.clients, name="Clients"),
    path('questions/', views.questions, name="Questions"),
    path('register/', views.register, name="Register"),


]
