"""Just user profiles here

"""
from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """User profile"""
    user = models.ForeignKey(User, unique=True, blank=True, null=True)
    name = models.CharField(max_length=64)
    surname = models.CharField("Last Name", max_length=64)
    bio = models.TextField()
    birth = models.DateField("Date of Birth")
    photo = models.ImageField(upload_to='photos', blank=True)

    def __unicode__(self):
        return self.name


class Contact(models.Model):
    """Any type of contact"""
    owner = models.ForeignKey(Profile)
    mean = models.CharField(max_length=16)
    data = models.CharField(max_length=255)

    def __unicode__(self):
        return "%s: %s" % (self.mean, self.data)
