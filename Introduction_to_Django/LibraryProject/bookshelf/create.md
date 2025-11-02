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
