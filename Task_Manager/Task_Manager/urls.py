"""
URL configuration for Task_Manager project.

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
# from django.contrib import admin
# from django.urls import path
# from home.views  import *

# urlpatterns = [
#     path('',home,name='home'),
#     path('admin/', admin.site.urls),
#     path('mypage/',myhome,name='myhome'),
#     path('mypages2/',mypages23,name='mypages23'),
#     path('mypages3/',myhome12,name='myhome12'),
#     path('sendobjs/',objectdispl,name='objectdispl')
# ]

from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from home.views import TaskDetailViewSet, home, myhome, mypages23, myhome12, objectdispl

# Create router and register viewsets
router = DefaultRouter()
router.register(r'taskdetails', TaskDetailViewSet)

urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('mypage/', myhome, name='myhome'),
    path('mypages2/', mypages23, name='mypages23'),
    path('mypages3/', myhome12, name='myhome12'),
    path('sendobjs/', objectdispl, name='objectdispl'),
    # Include router URLs
    path('api/', include(router.urls)),  # API routes prefixed with 'api/'
    path("abc/",include('home.myurls')),
]
