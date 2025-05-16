from django.contrib.auth.models import AbstractUser
from django.db import models


class Role(models.TextChoices):
    READER = ('reader','Reader')   # read,detail,
    ADMIN = ('admin','Admin')           # crud,
    WRITER = ('writer','Writer')          # update,read,

class CustomUser(AbstractUser):
    phone = models.CharField(max_length=11,blank=True,null=True)
    role=models.CharField(max_length=20,choices=Role,default=Role.READER)