from django.urls import path
from . import views

urlpatterns = [
    path('',views.shows),
    path('shows/new',views.create),
    path('add',views.add),
    path('shows/<int:id>',views.show_details),
    path('shows',views.shows),
    path('shows/<int:id>/edit',views.edit),
    path('update',views.update),
    path('shows/<int:id>/destroy',views.destroy)
]