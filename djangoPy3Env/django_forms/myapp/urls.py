from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('delete_all',views.delete_all),
    path('form1',views.show_form1),
    path('add1',views.add1),
    path('form2',views.show_form2),
    path('add2',views.add2),
    path('form3',views.show_form3),
    path('add3',views.add3),
]
