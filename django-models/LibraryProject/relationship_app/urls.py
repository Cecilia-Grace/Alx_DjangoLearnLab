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
    path('logout/', CustomLogoutView.as_view(template_name= 'login.html'), name='logout'),
    path('login/', CustomLoginView.as_view(template_name= 'logout.html'), name='login'),
]
