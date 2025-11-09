from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
from .models import Library
from .models import Book

# --- 1. Function-based View (FBV): List All Books ---
def book_list(request):
    """Lists all books and renders them using the list_books.html template."""
    
    # Retrieve all books from the database
    all_books = Book.objects.all().select_related('author')
    
    context = {
        'books': all_books,
        'app_name': 'Relationship App',
    }
    
    # Renders the HTML template using the list of books
    return render(request, 'relationship_app/list_books.html', context)


# --- 2. Class-based View (CBV): Library Detail ---
class LibraryDetailView(DetailView):
    """Displays details for a specific Library, listing all its books."""
    
    # Model to retrieve the object from
    model = Library
    
    # The primary key URL parameter will be named 'pk' by default, or 'id' if specified in urls.py
    # Here we assume the URL pattern uses the 'pk' parameter, e.g., library/1/
    
    # Template to use for rendering
    template_name = 'relationship_app/library_detail.html'
    
    # The context object will be named 'library' (lowercase model name) by default.
    
    # To ensure related books are loaded efficiently
    def get_queryset(self):
        return Library.objects.prefetch_related('books__author')

# Create your views here.
