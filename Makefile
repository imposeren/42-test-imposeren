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

syncdb:
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=$(PROJECT).settings $(MANAGE) syncdb --noinput #--migrate
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=$(PROJECT).settings $(MANAGE) loaddata auth.json

migrate:
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=$(PROJECT).settings $(MANAGE) syncdb --noinput --migrate
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=$(PROJECT).settings $(MANAGE) migrate
