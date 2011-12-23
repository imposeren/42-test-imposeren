"""Just user profiles here

"""

from django.db import models


class Profile(models.Model):
    """User profile"""
    name = models.CharField("First name", max_length=64)
    surname = models.CharField("Last Name", max_length=64)
    bio = models.TextField("Biogaphy")
    birth = models.DateField("Birth Date")


class Contact(models.Model):
    """Any type of contact"""
    owner = models.ForeignKey(Profile)
    mean = models.CharField(max_length=16)
    data = models.CharField(max_length=255)
