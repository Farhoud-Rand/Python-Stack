from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('checkout/post', views.checkout),
    path('checkout',views.show_checkout),
]
