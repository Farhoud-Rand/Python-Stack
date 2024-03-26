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
def add_book(request):
    if (request.method == 'POST'):
        title = request.POST['book_title']
        description = request.POST['book_desc']
        Book.objects.create(title = title, description = description)

# Function to get book by its ID
def get_book_by_id(id):
    return Book.objects.get(id = id)

# Function to return all authors
def get_all_authors():
    return Author.objects.all()

# function to add new author for a specific book
def add_author_for_book(request):
    if (request.method == 'POST'):
        author_id = int(request.POST['author'])
        author = get_author_by_id(author_id)
        book_id = int(request.POST['book'])
        book = get_book_by_id(book_id)
        book.authors.add(author)
#####################################################################
# Function to add new book
def add_author(request):
    if (request.method == 'POST'):
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        notes = request.POST['notes']
        Author.objects.create(first_name = first_name, last_name = last_name, notes = notes)

# Function to get author by its ID
def get_author_by_id(id):
    return Author.objects.get(id = id)

# function to add new book for a specific author
def add_book_for_author(request):
    if (request.method == 'POST'):
        author_id = int(request.POST['author'])
        author = get_author_by_id(author_id)
        book_id = int(request.POST['book'])
        book = get_book_by_id(book_id)
        author.books.add(book)