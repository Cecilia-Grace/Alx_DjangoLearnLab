>>> from bookshelf.models import Book
>>> book_to_delete = Book.objects.get(pk=1)
>>> book_to_delete.delete()
(1, {'bookshelf.Book': 1})
>>> books = Book.objects.all()
>>> print(f"Books left: {books}")
#Output
Books left: <QuerySet []>
