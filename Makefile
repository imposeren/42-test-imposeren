MANAGE=django-admin.py
TESTER=django-nosetests.py
PROJECT="testsite"
PPATH=`pwd`
#PYTHONPATH="${PYTHONPATH}:${PPATH}:${PPATH}/testsite"

test: collectstatic syncdb
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=${PROJECT}.settings ${TESTER} --with-coverage --cover-package=${PROJECT} ${PROJECT}

run: collectstatic
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=${PROJECT}.settings $(MANAGE) runserver

syncdb:
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=${PROJECT}.settings $(MANAGE) syncdb --noinput

collectstatic:
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=${PROJECT}.settings $(MANAGE) collectstatic --noinput

