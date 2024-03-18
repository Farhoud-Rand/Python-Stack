from . import views
from django.urls import path 

urlpatterns = [
    path('',views.root),
    path('new',views.new),
]