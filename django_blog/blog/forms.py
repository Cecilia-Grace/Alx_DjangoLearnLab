from django import forms
from django.contrib.auth.models import User
from .models import Post, Comment
from django.contrib.auth.forms import UserCreationForm


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name']


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']
        
        
class CommentForm(forms.ModelForm):
    content = forms.CharField(
    widget=forms.Textarea(attrs={'rows': 3, 'placeholder': 'Write your comment here...'}),
    max_length=1000,
    label=''
)

class Meta:
    model = Comment
    fields = ['content']