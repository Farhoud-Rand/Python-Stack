from django.db import models

# Book class
class Book(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# Author class
class Author(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 
    notes = models.TextField(default = "empty")
    books = models.ManyToManyField(Book, related_name='authors')

# Function to return all books
def get_all_books():
    return Book.objects.all()

# Function to add new book
def add_book(request_data):
    title = request_data['book_title']
    description = request_data['book_desc']
    Book.objects.create(title = title, description = description)

# Function to get book by its ID
def get_book_by_id(id):
    return Book.objects.get(id = id)

# Function to return all authors
def get_all_authors():
    return Author.objects.all()

# function to add new author for a specific book
def add_author_for_book(request_data):
    author_id = int(request_data['author'])
    author = get_author_by_id(author_id)
    book_id = int(request_data['book'])
    book = get_book_by_id(book_id)
    book.authors.add(author)
    return book_id

# Function to add new book
def add_author(request_data):
    first_name = request_data['first_name']
    last_name = request_data['last_name']
    notes = request_data['notes']
    Author.objects.create(first_name = first_name, last_name = last_name, notes = notes)

# Function to get author by its ID
def get_author_by_id(id):
    return Author.objects.get(id = id)

# Function to add new book for a specific author
def add_book_for_author(request_data):
    author_id = int(request_data['author'])
    author = get_author_by_id(author_id)
    book_id = int(request_data['book'])
    book = get_book_by_id(book_id)
    author.books.add(book)
    return author_id

# Function to get all the books that not in author books list
def get_all_book_not_in_author_books(id):
    author = get_author_by_id(id)
    author_books = author.books.all()
    return Book.objects.exclude(id__in=[book.id for book in author_books])

# Function to get all the authors that not in book authors list
def get_all_author_not_in_book_authors(id):
    book = get_book_by_id(id)
    book_authors = book.authors.all()
    return Author.objects.exclude(id__in=[book.id for book in book_authors])