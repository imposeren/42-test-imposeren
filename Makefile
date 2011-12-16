MANAGE=django-admin.py
TESTER=django-nosetests.py

test : syncdb
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=testsite.settings ${TESTER} testsite
#PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=testsite.settings $(MANAGE) test hello

run:
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=testsite.settings $(MANAGE) runserver

syncdb:
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=testsite.settings $(MANAGE) syncdb --noinput


