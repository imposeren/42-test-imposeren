"""Models go here"""
from django.db import models


class Request(models.Model):
    """Request item"""
    method = models.CharField(max_length=3)
    path = models.CharField(max_length=256)
    get = models.CharField(max_length=256)
    post = models.CharField(max_length=256)
    date = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return "%s: %s %s " % (self.date, self.method, self.path)


class Modellog(models.Model):
    """Log entry about database modification"""
    ACTION_CHOICES = (
        ('C', 'create'),
        ('E', 'edit'),
        ('D', 'delete'),
    )
    action = models.CharField(max_length=1, choices=ACTION_CHOICES)
    inst_pk = models.IntegerField()
    app = models.CharField(max_length=32, choices=ACTION_CHOICES)
    model = models.CharField(max_length=32, choices=ACTION_CHOICES)
    date = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return "%s: %s %s.%s, pk=%s " % (self.date, self.action, self.app,
                                         self.model, self.inst_pk)