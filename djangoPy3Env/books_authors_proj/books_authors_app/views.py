from django.shortcuts import render, redirect
from . import models 

# This function will show the root route that contains the books and add book form
def index(request):
    context = {
        'books': models.get_all_books(),
    }
    return render (request, "index.html", context) 

# This function is used to add a new book
def add_book(request):
    models.add_book(request)
    return redirect("/")

# This function is used to render a new page that shows the book information
def show_book_details(request, id):
    context = {
        'book': models.get_book_by_id(id),
        'authors':models.get_all_authors(),
        'not_in':models.get_all_author_not_in_book_authors(id),

    }
    return render (request, "show_book.html", context) 

# This function is used to add a new author for a specific book 
def add_author_for_book(request):
    id = str(models.add_author_for_book(request))
    return redirect("/books/"+id)

# This function will show all authors in the table and add author form
def show_authors(request):
    context = {
        'authors': models.get_all_authors(),
    }
    return render (request, "authors.html", context) 

# This function is used to add a new author
def add_author(request):
    models.add_author(request)
    return redirect("/authors")

# This function is used to render a new page that shows the author information
def show_author_details(request, id):
    context = {
        'author': models.get_author_by_id(id),
        'books':models.get_all_books(),
        'not_in':models.get_all_book_not_in_author_books(id),
    }
    return render (request, "show_author.html", context) 

# This function is used to add a new book for a specific author 
def add_book_for_author(request):
    id = str(models.add_book_for_author(request))
    return redirect("/authors/"+id)