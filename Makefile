MANAGE=django-admin.py
TESTER=django-nosetests.py
PROJECT=testsite

pretest:
	-rm $(PROJECT)/database_test.sqlite
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=$(PROJECT).settings_test $(MANAGE) syncdb --noinput
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=$(PROJECT).settings_test $(MANAGE) collectstatic --noinput

test: pretest 
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=$(PROJECT).settings_test $(TESTER) --with-coverage --cover-package=$(PROJECT) -e '._wm.*' $(PROJECT)

testall: pretest
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=$(PROJECT).settings_test $(TESTER) --with-coverage --cover-package=$(PROJECT)  $(PROJECT)

run: syncdb
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=$(PROJECT).settings $(MANAGE) collectstatic --noinput
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=$(PROJECT).settings $(MANAGE) runserver

syncdb: $(PROJECT)/database.sqlite
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=$(PROJECT).settings $(MANAGE) syncdb --noinput --migrate
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=$(PROJECT).settings $(MANAGE) loaddata auth.json

$(PROJECT)/database.sqlite:
	sed -i  -e "s/'south'/#'south'/" $(PROJECT)/settings.py
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=$(PROJECT).settings $(MANAGE) syncdb --noinput
	sed -i -e "s/\#'south'/'south'/" $(PROJECT)/settings.py
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=$(PROJECT).settings $(MANAGE) syncdb --noinput
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=$(PROJECT).settings $(MANAGE) migrate profiles 0001 --fake
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=$(PROJECT).settings $(MANAGE) migrate mylogging 0003 --fake

migrate:
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=$(PROJECT).settings $(MANAGE) syncdb --noinput --migrate
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=$(PROJECT).settings $(MANAGE) migrate
