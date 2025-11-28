from rest_framework import serializers
from .models import Author, Book
from datetime import date

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name']


class BookSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(queryset=Author.objects.all())
    
    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_year', 'author']
        
    def validate_published_year(self, value): #validation for year not to be in the future
        current_year = date.today().year
        if value > current_year:
            raise serializers.ValidationError("Kindly enter a valid year")
        return value



      

