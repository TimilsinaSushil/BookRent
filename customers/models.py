from django.db import models
from books.models import Book

# Create your models here.

class Customer(models.Model):
   first_name = models.CharField(max_length=100)
   last_name = models.CharField(max_length=100)
   username = models.CharField(max_length=100, blank=True, unique=True)
   additional_info = models.TextField(blank=True)
   rating = models.models.PositiveIntegerField(default=50)
   books = models.ManyToManyField(Book, blank=True, help_text='books that are currently rented')
