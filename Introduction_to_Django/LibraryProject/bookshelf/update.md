>>> from bookshelf.models import Book
>>> book = Book.objects.get(pk=1)
>>> book.title = "Nineteen Eighty-Four"
>>> book.save()
>>> print(f"Book updated. New title: {book.title}")
#Output
Book updated. New title: Nineteen Eighty-Four
