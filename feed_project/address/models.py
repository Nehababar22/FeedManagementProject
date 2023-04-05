from django.db import models
from django.conf import settings

# Create your models here.
class Address(models.Model):
    """ Address Model """

    street = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    country = models.CharField(max_length=20)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
