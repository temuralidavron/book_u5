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
    title=models.CharField(max_length=300,verbose_name='nomi')
    description=models.TextField()
    isbn=models.IntegerField()
    price=models.IntegerField()
    image=models.ImageField(upload_to='images',blank=True,null=True)
    author=models.ForeignKey(Author,on_delete=models.PROTECT,related_name='book_author',blank=True,null=True)
    file=models.FileField(upload_to='files',blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    @property
    def title_isbn(self):
        return f"{self.title} ning isbni {self.isbn}"





    def __str__(self):
        return self.title



class Product(models.Model):
    title=models.CharField(max_length=300,verbose_name='nomi')
    description=models.TextField()
    price=models.IntegerField()
    quantity=models.IntegerField()
    # total_price=models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    #
    # def save(self, *args, **kwargs):
    #     self.total_price=self.price*self.quantity
    #     super().save(*args, **kwargs)

    # @property
    # def total_price(self):
    #     return self.price * self.quantity

