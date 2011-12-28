MANAGE=django-admin.py
TESTER=django-nosetests.py
PROJECT=testsite
PPATH=`pwd`
#PYTHONPATH="${PYTHONPATH}:${PPATH}:${PPATH}/testsite"

test: collectstatic
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=${PROJECT}.settings_test ${MANAGE} syncdb --noinput
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=${PROJECT}.settings_test ${TESTER} --with-coverage --cover-package=${PROJECT} -e '._wm.*' ${PROJECT}
	rm ${PROJECT}/database_test.sqlite

testall:
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=${PROJECT}.settings_test ${MANAGE} syncdb --noinput
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=${PROJECT}.settings_test ${TESTER} --with-coverage --cover-package=${PROJECT}  ${PROJECT}
	rm ${PROJECT}/database_test.sqlite

run: collectstatic syncdb
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=${PROJECT}.settings ${MANAGE} runserver

syncdb:
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=${PROJECT}.settings ${MANAGE} syncdb --noinput --migrate

collectstatic:
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=${PROJECT}.settings ${MANAGE} collectstatic --noinput

migrate:
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=${PROJECT}.settings ${MANAGE} schemamigration profiles --auto
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=${PROJECT}.settings ${MANAGE} migrate profiles
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=${PROJECT}.settings ${MANAGE} schemamigration mylogging --auto
	PYTHONPATH=`pwd` DJANGO_SETTINGS_MODULE=${PROJECT}.settings ${MANAGE} migrate mylogging
