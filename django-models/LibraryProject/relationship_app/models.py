from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Author(models.Model):
    name = models.CharField(max_length = 200)
    
    def __str__(self):
        return self.name
    
    
class Book(models.Model):
    title = models.CharField(max_length = 200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name = "books")
    
    def __str__(self):
        return self.title
    

class Library(models.Model):
    name = models.CharField(max_length = 200)
    books = models.ManyToManyField(Book, related_name = "libraries")
    
    def __str__(self):
        return self.name
    
class Librarian(models.Model):
    name = models.CharField(max_length = 200)
    library = models.OneToOneField(Library, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name


class UserProfile(models.Model):
    ADMIN = 'Admin'
    LIBRARIAN = 'Librarian'
    MEMBER = 'Member'
    
    ROLE_CHOICES = [
        (ADMIN, 'Admin'),
        (LIBRARIAN, 'Librarian'),
        (MEMBER, 'Member'),
    ]
    
    # OneToOne relationship to Django's built-in User model
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    # CharField with predefined role choices, default to Member
    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default=MEMBER,
    )

    def __str__(self):
        return f"{self.user.username} - {self.role}"

# Signal function to create/update UserProfile whenever a User object is saved
@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        # Create a new profile if the User instance is newly created
        UserProfile.objects.create(user=instance)
    # Ensure profile exists and save if the User object is updated (e.g., in admin)
    instance.userprofile.save() 
    
    
# Create your models here.
