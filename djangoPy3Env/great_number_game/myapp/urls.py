from django.urls import path
from . import views

urlpatterns = [
    path('',views.welcome),
    path('easy',views.easy),
    path('hard',views.hard),
    path('guess_from_user',views.check_number),
    path('show_result',views.show),
    path('destroy_session',views.clear_session),
    path('leaderboard',views.leaderbord),
    path('show_leaderboard',views.show_leaderbord),
    path('back_home',views.back_home),
]