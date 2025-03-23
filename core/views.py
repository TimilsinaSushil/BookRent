# from django.http import HttpResponse
from django.shortcuts import render
from customers.models import Customer
from books.models import Book, BookTitle

def home_view(request):
    # return HttpResponse("<h1>hello world</h1> <p>Hi there</P>")
    qs = Customer.objects.all()
    # obj = Book.objects.get(id=1)
    obj = BookTitle.objects.get(id=11)
    books = obj.get_books()
    print(books)
    context = {
        'qs': qs,
        'obj': obj
    }
    return render(request, 'main.html', context)