from django.urls import path
# from .views import *
from .views import get_book
# from book import views

urlpatterns=[
    path('',get_book,name='book-list')
]