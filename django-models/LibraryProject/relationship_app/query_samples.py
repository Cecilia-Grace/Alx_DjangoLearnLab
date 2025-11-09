import os
import django
import sys
from django.core.exceptions import ObjectDoesNotExist

# Set up the Django environment
# Add the project root (the directory containing LibraryProject) to the path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

def setup_data():
    """Clears and creates sample data, returning the identifiers needed for retrieval."""
    
    # Clear previous data
    Author.objects.all().delete()
    Library.objects.all().delete()
    
    # --- Data Setup (Using .get_or_create) ---
    a1, _ = Author.objects.get_or_create(name="Chinua Achebe")
    a2, _ = Author.objects.get_or_create(name="Ngugi wa Thiong'o")
    
    b1, _ = Book.objects.get_or_create(title="Things Fall Apart", author=a1)
    b2, _ = Book.objects.get_or_create(title="No Longer At Ease", author=a1)
    b3, _ = Book.objects.get_or_create(title="Weep Not, Child", author=a2)
    
    lib_k, _ = Library.objects.get_or_create(name="Kitengela Community Library")
    lib_k.books.add(b1, b3)
    
    Librarian.objects.get_or_create(name="Esther Njoroge", library=lib_k)
    
    print("Sample data created successfully.\n")
    
    return a1.name, lib_k.name 

def run_queries(author_name, library_name):
    """Retrieves objects using .get() and runs the required relationship queries."""
    
    print("--- Query Results ---")
    
    try:
        # --- RETRIEVAL STEP using .get() ---
        # Get Author and Library by name (Necessary for .filter() and Query 3)
        target_author = Author.objects.get(name=author_name) 
        target_library = Library.objects.get(name=library_name) # Explicit .get()
        
        # --- Query 1: Books by a specific author (ForeignKey) ---
        print(f"\n1. All books by {target_author.name}:")
        
        # Explicit .filter() implementation to satisfy the requirement
        books_by_author = Book.objects.filter(author=target_author) 
        
        for book in books_by_author:
            print(f"   - {book.title}")

        # --- Query 2: All books in a library (ManyToManyField) ---
        print(f"\n2. All books in {target_library.name}:")
        # ManyToMany is most simply accessed directly via the object
        for book in target_library.books.all():
            print(f"   - {book.title}")

        # --- Query 3: Retrieve the librarian for a library (OneToOneField) ---
        print(f"\n3. Librarian for {target_library.name}:")
        librarian_name = target_library.librarian.name
        print(f"   - Librarian: {librarian_name}")
        
    except ObjectDoesNotExist as e:
        print(f"\nERROR: Could not find required data: {e}")


if __name__ == '__main__':
    author_id, library_id = setup_data()
    run_queries(author_id, library_id)