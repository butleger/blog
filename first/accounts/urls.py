from django.contrib import admin
from django.urls import path
from django.urls import include
from . import views

app_name = 'accounts'
urlpatterns = [
    path('registration/', views.registrate, name='register_user'),
    path('login/', views.MyLoginView.as_view(), name='login'),
    path('logout/', views.MyLogoutView.as_view(), name='logout'),
    path('success_login/', views.MySuccesLoginView.as_view(), name='success_login')
]