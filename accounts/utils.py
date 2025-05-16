from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import redirect

from accounts.models import Role, CustomUser
from book.models import Book


def ulu_barsa(func):
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect("login")
        return func(request, *args, **kwargs)
    return wrapper


def checking_admin(func):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.role==Role.ADMIN:
                return func(request, *args, **kwargs)
            else:
                return redirect("login")
    return wrapper

content=ContentType.objects.get_for_model(Book)
permission=Permission.objects.get(codename='view_book')

group,created =Group.objects.get_or_create(name="Published")
user=CustomUser.objects.get(username='baxtitashkent')
user.groups.add(group)
group.permissions.add(permission)