#!/usr/bin/env bash
set -x

function do_db() {
    python test_project/manage.py syncdb --traceback --noinput --settings=test_project.$1
    python test_project/manage.py migrate --noinput --traceback --settings=test_project.$1
    python test_project/manage.py cities_light --force-import-all --traceback --settings=test_project.$1
}

pip install south psycopg2

if [[ ${TRAVIS_PYTHON_VERSION%%.*} -eq "2" ]]; then
    # test on mysql
    pip install mysql-python 
    do_db settings_mysql
fi

# test on postgres
do_db settings_postgres

# test on sqlite
rm -rf test_project/db.sqlite
do_db settings
