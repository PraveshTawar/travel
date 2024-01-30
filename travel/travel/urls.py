"""
URL configuration for travel project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from home.views import *
from django.contrib.auth.views import PasswordChangeView ,PasswordChangeDoneView 
# from django.contrib.auth.forms import PasswordChangeForm
from home.form import MyChangeForm



urlpatterns = [
    path('home/', Home ),
    path('', signup),
    path('login/', login_page),
    path('logout/', logout_page),
    path('change-password/',PasswordChangeView.as_view(template_name="change-password.html",form_class= MyChangeForm),name='change-password'),
    path('password-change-done/',PasswordChangeDoneView.as_view(template_name="change_done.html"),name='password_change_done'),
    
    
    
    path('admin/', admin.site.urls),
]
