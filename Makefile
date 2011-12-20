MANAGE=django-admin.py
TESTER=django-nosetests.py
PROJECT="testsite"
PPATH="`pwd`:`pwd`:/${PROJECT}"
#PYTHONPATH="${PYTHONPATH}:${PPATH}:${PPATH}/testsite"

test : syncdb
	PYTHONPATH="${PYTHONPATH}:${PPATH}" DJANGO_SETTINGS_MODULE=${PROJECT}.settings ${TESTER} ${PROJECT}
#PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=testsite.settings $(MANAGE) test hello

run: collectstatic
	PYTHONPATH="${PYTHONPATH}:${PPATH}" DJANGO_SETTINGS_MODULE=${PROJECT}.settings $(MANAGE) runserver

syncdb:
	PYTHONPATH="${PYTHONPATH}:${PPATH}" DJANGO_SETTINGS_MODULE=${PROJECT}.settings $(MANAGE) syncdb --noinput

collectstatic:
	PYTHONPATH="${PYTHONPATH}:${PPATH}" DJANGO_SETTINGS_MODULE=${PROJECT}.settings $(MANAGE) collectstatic --noinput


