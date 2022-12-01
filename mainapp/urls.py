from django.urls import path

from mainapp import views

urlpatterns = [
    path('', views.homeview, name="homepage"),
    path('login/', views.loginview, name="loginpage"),
    path('register/', views.registerview, name="registerpage"),
    path('logout/', views.logoutview, name="logoutpage"),
]