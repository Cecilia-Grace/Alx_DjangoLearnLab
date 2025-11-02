>>> from bookshelf.models import Book
>>> book = Book.objects.get(pk=1)
>>> book.delete()
(1, {'bookshelf.Book': 1})
>>> books = Book.objects.all()
>>> print(f"Books left: {books}")
#Output
Books left: <QuerySet []>
