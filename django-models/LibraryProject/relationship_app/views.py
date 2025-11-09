from django.views.generic.detail import DetailView
from .models import Library
from .models import Book
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import DetailView
from django.views import View
from django.http import HttpResponse
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render
from .models import UserProfile

# Re-including previous views for context (assuming you kept the HTML template version)
from .models import Book, Library # Assuming models are imported for previous tasks

# Function-based View (FBV) for listing books (using HTML template from previous task)
def book_list(request):
    # ... (content of book_list view here)
    pass # Placeholder for existing view

# Class-based View (CBV) for library detail (using HTML template from previous task)
class LibraryDetailView(DetailView):
    # ... (content of LibraryDetailView here)
    pass # Placeholder for existing view


# --- New Authentication Views ---

# 1. Registration View (Custom Function)
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to the login page after successful registration
            return redirect('login') 
    else:
        form = UserCreationForm()
    
    # Renders the registration form
    return render(request, 'relationship_app/register.html', {'form': form})

# 2. Login View (Built-in)
class CustomLoginView(LoginView):
    template_name = 'login.html'
    fields = '__all__'
    redirect_authenticated_user = True
    
    # Optional: Customize success URL (default is settings.LOGIN_REDIRECT_URL)
    # def get_success_url(self):
    #     return reverse_lazy('book-list')

# 3. Logout View (Built-in)
class CustomLogoutView(LogoutView):
    # Optional: Customize the page shown after logout (default is settings.LOGOUT_REDIRECT_URL)
<<<<<<< HEAD
    template_name = 'relationship_app/logout.html'
=======
    template_name = 'logout.html'
    
    
def is_admin(user):
    # Checks if the user is authenticated AND has the 'Admin' role
    return user.is_authenticated and user.userprofile.role == UserProfile.ADMIN

def is_librarian(user):
    # Checks if the user is authenticated AND has the 'Librarian' role
    return user.is_authenticated and user.userprofile.role == UserProfile.LIBRARIAN

def is_member(user):
    # Checks if the user is authenticated AND has the 'Member' role
    return user.is_authenticated and user.userprofile.role == UserProfile.MEMBER

# --- Role-Restricted Views ---

@user_passes_test(is_admin, login_url='/relationship/login/') 
def admin_view(request):
    """View accessible only by Admin users."""
    return render(request, 'relationship_app/admin_view.html', {'role': 'Admin'})

@user_passes_test(is_librarian, login_url='/relationship/login/')
def librarian_view(request):
    """View accessible only by Librarian users."""
    return render(request, 'relationship_app/librarian_view.html', {'role': 'Librarian'})

@user_passes_test(is_member, login_url='/relationship/login/')
def member_view(request):
    """View accessible only by Member users."""
    return render(request, 'relationship_app/member_view.html', {'role': 'Member'})
>>>>>>> 1ae4096 (initial commit)
