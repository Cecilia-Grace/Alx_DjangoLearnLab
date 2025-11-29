from django.urls import path, include
from .views import BookListView, BookCreateView, BookDeleteView, BookDetailView, BookUpdateView

urlpatterns = [
    path('books/', BookListView.as_view(), name='book-list'),
    path('books/add', BookCreateView.as_view(), name='add-book'),
    path('books/<int:pk>/delete/', BookDeleteView.as_view(), name='delete-book'),
    path('/books/<int:pk>/', BookDetailView.as_view(), name='retrieve-book'),
    path('books/<int:pk>/update/', BookUpdateView.as_view(), name='update-book'),
]
