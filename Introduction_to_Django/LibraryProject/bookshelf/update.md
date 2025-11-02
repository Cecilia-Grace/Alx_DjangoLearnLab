>>> from bookshelf.models import Book
>>> book_to_update_title = Book.objects.get(pk=1)
>>> book_to_update_title.title = "Nineteen Eighty-Four"
>>> book_to_update_title.save()
>>> print(f"Book updated. New title: {book_to_update_title.title}")
#Output
Book updated. New title: Nineteen Eighty-Four
