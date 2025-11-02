>>> from bookshelf.models import Book
>>> book = Book.objects.get()
>>> print(f"Retrieved book. Title: {book.title}, Author: {book.author}, Publication year: {book.publication_year}")
#Output
Retrieved book. Title: 1984, Author: George Orwell, Publication year: 1949
