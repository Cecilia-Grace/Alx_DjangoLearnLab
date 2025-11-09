# relationship_app/urls.py

from django.urls import path
from .views import list_books
from . import views
from .views import CustomLoginView, CustomLogoutView, LibraryDetailView

urlpatterns = [
    path('books/', views.book_list, name='book-list'),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library-detail'),
    # Registration
    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
