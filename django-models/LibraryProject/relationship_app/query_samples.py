import os
import django
import sys

# Set up the Django environment
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

def run_queries_and_setup():
    """Sets up data, runs required queries, and prints results."""
    
    # Clear previous data
    Author.objects.all().delete()
    Library.objects.all().delete()
    
    # --- Data Setup ---
    
    # 1. Authors
    a1, _ = Author.objects.get_or_create(name="Chinua Achebe")
    a2, _ = Author.objects.get_or_create(name="Ngugi wa Thiong'o")
    
    # 2. Books (ForeignKey)
    b1, _ = Book.objects.get_or_create(title="Things Fall Apart", author=a1)
    b2, _ = Book.objects.get_or_create(title="No Longer At Ease", author=a1)
    b3, _ = Book.objects.get_or_create(title="Weep Not, Child", author=a2)
    
    # 3. Library (ManyToMany)
    lib_k, _ = Library.objects.get_or_create(name="Kitengela Community Library")
    lib_k.books.add(b1, b3)
    
    # 4. Librarian (OneToOne)
    Librarian.objects.get_or_create(name="Esther Njoroge", library=lib_k)
    
    print("--- Query Results ---")
    
    # --- Query 1: Books by a specific author (Chinua Achebe) ---
    print(f"\n1. All books by {a1.name}:")
    for book in a1.books.all():
        print(f"   - {book.title}")

    # --- Query 2: All books in a library ---
    print(f"\n2. All books in {lib_k.name}:")
    for book in lib_k.books.all():
        print(f"   - {book.title}")

    # --- Query 3: Retrieve the librarian for a library ---
    print(f"\n3. Librarian for {lib_k.name}:")
    try:
        librarian_name = lib_k.librarian.name
        print(f"   - Librarian: {librarian_name}")
    except Librarian.DoesNotExist:
        print("   - No librarian found for this library.")


if __name__ == '__main__':
    run_queries_and_setup()