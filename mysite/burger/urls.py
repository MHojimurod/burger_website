from django.urls import path
from . import views


urlpatterns = [
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('recipe/',views.recipe,name='recipe'),
    path('blog/',views.blog,name='blog'),
    path('contact/',views.contact,name='contact'),
    path('signup/',views.signup,name='signup'),
]