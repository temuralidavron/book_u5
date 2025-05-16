from django.contrib.auth.decorators import login_required, permission_required
from django.core.mail import send_mail
from django.core.paginator import Paginator
from django.db.models import Sum, Q
from django.http import HttpResponse
from django.shortcuts import render, redirect

from accounts.utils import ulu_barsa, checking_admin
from .forms import BookForm, EmailForm
from .models import Book

#
# def get_book(request):
#     q=request.GET.get('q')
#     books=Book.objects.all()
#     if q:
#         books=books.filter(Q(title__icontains=q) | Q(description__icontains=q))
#     else:
#         books=books.all()
#     paginator = Paginator(books, 4)
#     page = request.GET.get('page')
#     page_obj = paginator.get_page(page)
#
#     context={
#         'books':books,
#         'page_obj':page_obj,
#     }
#     return render(request,'book/book_list.html',context)
def get_book(request):
    q = request.GET.get('q')
    books = Book.objects.all()

    if q:
        books = books.filter(Q(title__icontains=q) | Q(description__icontains=q))

    paginator = Paginator(books, 2)
    page = request.GET.get('page')
    page_obj = paginator.get_page(page)

    context = {
        'books': page_obj,  # MUHIM: sahifalangan obyektni uzatamiz
        'page_obj': page_obj,
    }
    return render(request, 'book/book_list.html', context)

# @login_required
@ulu_barsa
def book_detail(request,pk):
    book=Book.objects.get(pk=pk)
    context={
        'book':book
    }
    return render(request,'book/book_detail.html',context)


@checking_admin
def create_book(request):
    print(request.POST)
    if request.method=='POST':
        form=BookForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('book-list')
        # else:
        #     return HttpResponse('Invalid credentials xatolik ', status=401)
    else:
        form=BookForm()

    return render(request, 'book/create_book.html', {'form': form})


@ulu_barsa
def update_book(request,pk):
    book=Book.objects.get(pk=pk)
    if request.method=='POST':
        form=BookForm(request.POST,request.FILES,instance=book)
        if form.is_valid():
            form.save()
            return redirect('book-list')
        else:
            return HttpResponse('Invalid credentials', status=401)
    else:
        form=BookForm(instance=book)
    return render(request, 'book/create_book.html', {'form': form})

@permission_required('book.delete_book', raise_exception=True)
def delete_book(request,pk):
    book=Book.objects.get(pk=pk)
    if request.method=='POST':
        book.delete()
        return redirect('book-list')
    else:
        return render(request, 'book/book_delete.html', {'book': book})




def email_chat(request):
    if request.method == 'POST':
        form=EmailForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            from_email = form.cleaned_data['from_email']
            to_email = form.cleaned_data['to_email']
            send_mail(
                subject,
                message,
                from_email,
                [to_email],
            )
            return redirect('book-list')
    form=EmailForm()
    return render(request, 'book/email_chat.html', {'form': form})


