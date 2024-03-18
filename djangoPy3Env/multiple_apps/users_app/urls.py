from . import views
from django.urls import path 

urlpatterns = [
    path('register',views.register),
    path('login',views.login),
    path('users/new',views.register),
    path('users',views.root),
]