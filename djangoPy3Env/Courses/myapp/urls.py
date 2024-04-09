from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('add',views.add),
    path('courses/<int:id>', views.show_comments),
    path('courses/<int:id>/add/comment',views.add_comment),
    path('courses/destroy/<int:id>',views.delete_course),
]
