from django.db import models
from django.conf import settings

# Create your models here.
class Feed(models.Model):
    """ Feed Model """

    title = models.CharField(max_length=320)
    content = models.TextField()
    image = models.ImageField()
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
