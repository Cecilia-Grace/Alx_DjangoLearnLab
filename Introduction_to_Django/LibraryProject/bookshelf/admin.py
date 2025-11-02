from django.contrib import admin
from .models import Book

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



# Register your models here.
