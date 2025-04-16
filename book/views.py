from django.shortcuts import render

from .models import Book


def get_book(request):
    books=Book.objects.all()
    context={
        'books':books
    }
    return render(request,'book/book_list.html',context)