# -*- coding: utf-8 -*-
"""Command that prints all project models and the count of objects in every
model

"""
from django.core.management.base import NoArgsCommand
from django.db import models
import sys


def get_app_label(app):
    return '.'.join(app.__name__.split('.')[0:-1])


class Command(NoArgsCommand):
    help = """Command that prints all project models and the count of objects
    in every model

"""

    def handle_noargs(self, **options):
        for model in models.get_models():
            model_name = str(model).split("'")[1]
            model_objects = model.objects.count()
            message = "model '%s': %d objects" % (model_name, model_objects)
            sys.stdout.write("%s\n" % message)
            sys.stderr.write("error: %s\n" % message)

