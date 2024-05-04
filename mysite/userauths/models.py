from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    
    USER_TYPE_CHOICES = [
        ('student', 'Student'),
        ('relationship_manager', 'Relationship Manager'),
    ]
    
    email = models.EmailField(unique=True)
    username = models.CharField(max_length = 100)
    bio = models.CharField(max_length = 100)
    user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES, default = 'student')

    #username = email
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username
    