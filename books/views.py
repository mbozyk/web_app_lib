from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from books.models import Book


# Create your views here.
def hello_world(request):
    our_context = {"time": datetime.now()}
    return render(request, template_name = "hello.html", context = our_context)
def title_site(request):
    return render(request, template_name = "index.html")
def adding(request):
    return render(request, template_name = "add.html")
def list_books(request):
    books = Book.objects.all()
    return render(request, template_name = "book_list.html", context = {"books":books})

