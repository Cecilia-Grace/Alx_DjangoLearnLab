# relationship_app/urls.py

from django.urls import path
from .views import book_list
from . import views
from .views import CustomLoginView, CustomLogoutView, LibraryDetailView

urlpatterns = [
    path('books/', views.book_list, name='book-list'),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library-detail'),
    # Registration
    path('register/', views.register, name='register'),
    path('logout/', CustomLogoutView.as_view(template_name= 'login.html'), name='logout'),
    path('login/', CustomLoginView.as_view(template_name= 'logout.html'), name='login'),
    path('admin_page/', views.admin_view, name='admin_view'),
    path('librarian_page/', views.librarian_view, name='librarian_view'),
    path('member_page/', views.member_view, name='member_view'),
    path('books/add/', views.add_book, name='book-add'),
    path('books/edit/<int:pk>/', views.edit_book, name='book-edit'),
    path('books/delete/<int:pk>/', views.delete_book, name='book-delete'),
]
