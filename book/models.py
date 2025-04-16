from django.db import models


class Author(models.Model):
    full_name=models.CharField(max_length=255)
    birth_day=models.DateField()
    country=models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.full_name


class Book(models.Model):
    title=models.CharField(max_length=300)
    description=models.TextField()
    isbn=models.IntegerField()
    price=models.IntegerField()
    author=models.ForeignKey(Author,on_delete=models.PROTECT,related_name='book_author')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



    def __str__(self):
        return self.title
