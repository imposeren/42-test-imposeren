"""Models go here"""
from django.db import models


class Request(models.Model):
    """Request item"""
    method = models.CharField(max_length=3)
    path = models.CharField(max_length=256)
    get = models.CharField(max_length=256)
    post = models.CharField(max_length=256)
    date = models.DateTimeField(auto_now_add=True)
