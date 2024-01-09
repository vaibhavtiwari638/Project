from tokenize import Name
from unicodedata import name
from django.urls import path
from Myapp.views import *
urlpatterns=[
    path('home',homepage,name='home'),
    path('Check',Predict,name='Check'),
    path('login',login,name='login'),
    path('signin',fun1,name="login"),
    path('signup',fun2,name="login"),
]