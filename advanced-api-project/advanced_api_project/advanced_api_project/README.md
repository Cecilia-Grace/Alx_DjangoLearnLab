API Views Overview

This project provides a simple API for managing Books using Django REST Framework (DRF). Each view is designed to handle a specific action (list, create, retrieve, update, delete) on Book instances.

Views Configuration
1. BookListView

Type: generics.ListAPIView

Purpose: Returns a list of all books in the database.

Configuration:

queryset = Book.objects.all() → Retrieves all books.

serializer_class = BookSerializer → Serializes book objects into JSON.

Behavior:

Read-only.

Can be accessed by unauthenticated users (if permissions allow).

2. BookDetailView

Type: generics.RetrieveAPIView

Purpose: Retrieves details of a single book by its ID (pk).

Configuration:

queryset = Book.objects.all() → Ensures lookup can be done across all books.

serializer_class = BookSerializer

Behavior:

Read-only.

Returns a 404 error if the book ID does not exist.

3. BookCreateView

Type: generics.CreateAPIView

Purpose: Allows creating a new book.

Configuration:

queryset = Book.objects.all()

serializer_class = BookSerializer

Behavior:

Accepts POST requests with book data in JSON format.

Validates fields like publication_year to prevent invalid data (e.g., future years).

Custom Hooks / Settings:

Serializer validation ensures publication_year is not greater than the current year.

4. BookUpdateView

Type: generics.UpdateAPIView

Purpose: Updates an existing book by ID.

Configuration:

queryset = Book.objects.all()

serializer_class = BookSerializer

Behavior:

Accepts PUT/PATCH requests.

Partial updates allowed using PATCH.

Custom Hooks / Settings:

Reuses serializer validation for consistent data integrity.

5. BookDeleteView

Type: generics.DestroyAPIView

Purpose: Deletes a book by ID.

Configuration:

queryset = Book.objects.all()

serializer_class = BookSerializer

Behavior:

Accepts DELETE requests.

Returns a confirmation on successful deletion or 404 if the book does not exist.

Custom Settings & Hooks

Serializer Validation

BookSerializer includes validate_publication_year() to ensure no future year can be saved.

Primary Key Related Field

The author field uses PrimaryKeyRelatedField to simplify POST/PUT requests with author ID.

URL Routing

Each view is mapped to a specific endpoint in api/urls.py.

Example: books/<int:pk>/update/ for updating a book.

Permissions

By default, read-only views (List and Detail) can be exposed to unauthenticated users.

Create, update, and delete actions can be restricted to authenticated users using DRF’s permissions classes.
