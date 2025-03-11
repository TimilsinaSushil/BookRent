# from django.http import HttpResponse
from django.shortcuts import render

def home_view(request):
    # return HttpResponse("<h1>hello world</h1> <p>Hi there</P>")
    value = "hello world 5"
    return render(request, 'main.html', { 'value':value  })