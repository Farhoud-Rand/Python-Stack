from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('add_two',views.add2),
    path('reset',views.reset),
    path('destroy_session',views.clear_session),
    path('increment_by',views.increment_by),
    path('counter',views.display_page),
]
