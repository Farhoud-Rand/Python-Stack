from django.urls import path 
from . import views

urlpatterns = [
    path('',views.index),
    path('add_book',views.add_book),
    path('books/<int:id>',views.show_book_details),
    path('add_author_for_book',views.add_author_for_book),
    path('authors',views.show_authors),
    path('add_author',views.add_author),
    path('authors/<int:id>',views.show_author_details),
    path('add_book_for_author',views.add_book_for_author),
]