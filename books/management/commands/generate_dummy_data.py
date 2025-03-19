from django.core.management.base import BaseCommand
from authors.models import Author
from publishers.models import Publisher
from books.models import BookTitle, Book
from customers.models import Customer
from django_countries.fields import Country
import random

class Command(BaseCommand):
    
    help = "generate dummy data  for  testing purpose"


    def handle(self, *args, **kwargs):

        #generating  authors
        authors_list = ['John Snmith', 'Adam Jones', 'Jane Johnson', 'Megan Hug']

        for name in authors_list:
            Author.objects.create(name = name)
            
        #generating publishers
        publishers_list = [
            {'name': 'Muna Madan', 'country':Country(code='us')},
            {'name': 'Radha Krishna', 'country':Country(code='de')},
            {'name': 'Raktapat', 'country':Country(code='gb')},
            {'name': 'Sunaulo Udan', 'country':Country(code='pl')}
        ]

        for item in publishers_list:
            Publisher.objects.create(**item)

        #generating book titles
        book_titles_list = ['Harry Zotter','Lord of the wings','Django Made Easy', 'Switcher']
        publishers = Publisher.objects.all()
        authors = list(Author.objects.all())
        items = zip(book_titles_list, publishers)

        for item in items:
            author = random.choice(authors)
            publisher = item[1]
            BookTitle.objects.create(title = item[0], publisher=publisher, authors=author)

        

        #generating books
        book_titles = BookTitle.objects.all()
        for title in book_titles:
            quantity = random.randint(1,5)
            for i in range(quantity):
                Book.objects.create(title=title)

        #generating customers
        customers_list = [
            { 'first_name': 'John', 'last_name':'doe' },
            { 'first_name': 'Adam', 'last_name':'Harris' },
            { 'first_name': 'Liza', 'last_name':'Martinez' }
        ]

        for item in customers_list:
            Customer.objects.create(**item)

    
   