#Python command
>>> from bookshelf.models import Book
>>> book1 = Book.objects.create(
...  title = "1984",
...  author = "George Orwell",
...  publication_year = 1949
... )
>>> print(f"Book Created. Title: {book1.title}, Author: {book1.author}, Publication year: {book1.publication_year} ")
#Output
Book Created. Title: 1984, Author: George Orwell, Publication year: 1949 
>>> from bookshelf.models import Book
>>> book = Book.objects.get()
>>> print(f"Retrieved book. Title: {book.title}, Author: {book.author}, Publication year: {book.publication_year}")
#Output
Retrieved book. Title: 1984, Author: George Orwell, Publication year: 1949
>>> from bookshelf.models import Book
>>> book_to_update_title = Book.objects.get(pk=1)
>>> book_to_update_title.title = "Nineteen Eighty-Four"
>>> book_to_update_title.save()
>>> print(f"Book updated. New title: {book_to_update_title.title}")
#Output
Book updated. New title: Nineteen Eighty-Four
>>> from bookshelf.models import Book
>>> book_to_delete = Book.objects.get(pk=1)
>>> book_to_delete.delete()
(1, {'bookshelf.Book': 1})
>>> books = Book.objects.all()
>>> print(f"Books left: {books}")
#Output
Books left: <QuerySet []>
