#!/bin/sh

echo "DATABASE"
echo $DATABASE
echo "POSTGRES_HOST"
echo $POSTGRES_HOST
echo "POSTGRES_PORT"
echo $POSTGRES_PORT

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $POSTGRES_HOST $POSTGRES_PORT; do
      echo "Waiting for postgres..."
      sleep 1
    done

    echo "PostgreSQL started"
fi


function postgres_ready(){
python << END
import sys
import psycopg2
import os
try:
    dbname = os.environ.get('POSTGRES_DB')
    user = os.environ.get('POSTGRES_USER')
    password = os.environ.get('POSTGRES_PASSWORD')
    host = os.environ.get('POSTGRES_HOST')
    conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host, port=5432)
except psycopg2.OperationalError:
    sys.exit(-1)
sys.exit(0)
END
}

until postgres_ready; do
  >&2 echo "Postgres is unavailable - sleeping"
  sleep 1
done

>&2 echo "Postgres is up - continuing..."

# python manage.py flush --no-input
# python manage.py migrate

exec "$@"