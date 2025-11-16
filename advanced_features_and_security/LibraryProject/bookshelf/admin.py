from django.contrib import admin
from .models import Book
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class BookAdmin(admin.ModelAdmin):
    # (the main table)
    list_display = ('title', 'author', 'publication_year', 'id')

    # Adds filter options to the right sidebar in the change list view
    list_filter = ('author', 'publication_year')

    # Adds a search bar 
    search_fields = ('title', 'author')

    # Make publication_year a column that can be edited directly on the list page
    list_editable = ('publication_year',)

# 2. Register the Book model with the custom configuration
admin.site.register(Book, BookAdmin)

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('email', 'username', 'date_of_birth', 'is_staff')
    fieldsets = UserAdmin.fieldsets + (
        ('Additional Info', {'fields': ('date_of_birth', 'profile_photo')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Additional Info', {'fields': ('date_of_birth', 'profile_photo')}),
    )


admin.site.register(CustomUser, CustomUserAdmin)

# Register your models here.
