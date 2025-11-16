# bookshelf/forms.py
from django import forms
from .models import Book

class ExampleForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'description', 'cover_image']  # adjust fields

    def clean_title(self):
        title = self.cleaned_data.get('title', '').strip()
        # simple validation example
        if '<script' in title.lower():
            raise forms.ValidationError("Invalid characters in title.")
        return title
