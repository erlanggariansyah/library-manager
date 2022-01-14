from django.shortcuts import render
from django.http import HttpResponse
from .models import Book

# Create your views here.

def bookView(request):
    books = Book.objects.all()
    data = {
        'books': books
    }

    return render(request, 'view/books.html', data)
