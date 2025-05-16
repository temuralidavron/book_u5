from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
# from .views import *
from .views import get_book,book_detail
from book import views
from .utils import send_email_u5

urlpatterns=[
    path('',get_book,name='book-list'),
    path('detail/<int:pk>/',book_detail,name='book-detail'),
    path('update/<int:pk>/',views.update_book,name='book-update'),
    path('delete/<int:pk>/',views.delete_book,name='book-delete'),
    path('create/',views.create_book,name='book-create'),
    path('send/',send_email_u5,name='send'),
    path('email/',views.email_chat,name='email'),
]