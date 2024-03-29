from django.contrib import admin
from django.urls import path
from .views import *
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path("about", views.about, name="about me"),
    path("contact", views.contact, name="contact me"),
    path("search", views.search, name="search"),
    path("vehicles", views.vehicles, name=" vehicles"),
    path("signup", views.handleSignup, name=" handleSignup"),
    path("login", views.handleLoginn, name=" handleLoginn"),
    path("logout", views.handleLogout, name=" handleLogout"),
    path("userpage",views.userpage, name="userpage"),
    path("navbar",views.navbar, name="navbar")


]