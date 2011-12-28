#!/bin/sh
DATE=`date +%F`
MANAGE=django-admin.py
PROJECT=testsite
PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=${PROJECT}.settings ${MANAGE} modelstats 2>./$DATE.dat
