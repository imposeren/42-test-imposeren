MANAGE=django-admin.py
TESTER=django-nosetests.py
PROJECT=testsite

test: 
	/bin/true

testall:
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=$(PROJECT).settings $(TESTER) --with-coverage --cover-package=$(PROJECT)  $(PROJECT)

run: syncdb $(PROJECT)/media $(PROJECT)/static
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=$(PROJECT).settings $(MANAGE) collectstatic --noinput
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=$(PROJECT).settings $(MANAGE) runserver

syncdb: $(PROJECT)/database.sqlite
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=$(PROJECT).settings $(MANAGE) syncdb --noinput --migrate
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=$(PROJECT).settings $(MANAGE) loaddata auth.json

$(PROJECT)/media:
	-mkdir $(PROJECT)/media

$(PROJECT)/static:
	-mkdir $(PROJECT)/static

$(PROJECT)/database.sqlite:
	-find . -name '*.pyc' | xargs rm
	-rm $(PROJECT)/settings.pyc
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=$(PROJECT).settings $(MANAGE) syncdb --noinput
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=$(PROJECT).settings $(MANAGE) syncdb --noinput
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=$(PROJECT).settings $(MANAGE) migrate profiles 0001 --fake
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=$(PROJECT).settings $(MANAGE) migrate mylogging 0003 --fake

migrate:
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=$(PROJECT).settings $(MANAGE) syncdb --noinput --migrate
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=$(PROJECT).settings $(MANAGE) migrate
