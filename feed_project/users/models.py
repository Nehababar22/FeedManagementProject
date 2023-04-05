from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    """ User Model """

    email = models.EmailField(unique=True)
    first_name=models.CharField(max_length=10)
    last_name=models.CharField(max_length=10)
