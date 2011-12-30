"""Models go here"""
from django.db import models
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.contrib.contenttypes.models import ContentType


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

    class Meta:
        get_latest_by = "date"

    def __unicode__(self):
        return "%s: %s %s.%s, pk=%s " % (self.date, self.action, self.app,
                                         self.model, self.inst_pk)


# Signals
# I don't like putting it in separate file and importing here because this will
# require recursive import (from testsite.mylogging import Modellog)
def log_any(sender, instance, action):
    instance_type = ContentType.objects.get_for_model(instance)
    app = instance_type.app_label
    if sender != Modellog and app != 'sessions':  # don't need to log sessions?
        newentry = Modellog()
        newentry.inst_pk = instance.pk
        newentry.app = app
        newentry.model = instance_type.model
        newentry.action = action
        newentry.save()


@receiver(post_save)
def log_edit_create(sender, instance, created, raw, **kwargs):
    if created:
        action = 'C'
    else:
        action = 'E'
    log_any(sender, instance, action)


@receiver(post_delete)
def log_delete(sender, instance, **kwargs):
    log_any(sender, instance, 'D')
