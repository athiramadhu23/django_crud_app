"""logn URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.urls import path
from django.contrib import admin
from home.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', login, name='login'),
    path('', log, name='log'),
    path('next/', second, name='next'),
    path('add/', add, name='add'),
    path('addstud/', add_stud, name='addstud'),
    path('viewstud/', view_stud, name='viewstud'),
    path('delete/<int:id>', delete, name='delete'),
    path('emp/', emp, name='emp'),
    path('viewemp/', view_emp, name='viewemp'),
    path('empdelete/<int:id>', emp_delete, name='empdelete'),
    path('stuedit/<int:id>', stu_edit, name='stuedit'),
    path('signup/',sign, name='signup'),
    path('otp/',otp, name='otp'),
]
