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
    path('addblog/', views.add_blog, name="addblog"),
    path('<int:pk>/editblog/', views.edit_blog, name="edit_blog"),
    path('<int:pk>/deleteblog/', views.delete_blog, name="delete_blog"),
    path('addfood/', views.add_about_food, name="addfood"),
    path('<int:pk>/editfood/', views.edit_about_food, name="edit_food"),
    path('<int:pk>/deletefood/', views.delete_about_food, name="delete_food"),


]
