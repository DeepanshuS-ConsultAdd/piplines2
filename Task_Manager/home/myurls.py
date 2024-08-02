from django.urls import path, include
from home.views import *

urlpatterns = [
    path("post1/",checks1,name='checks1')
]