#!/bin/sh
echo 'Run migration'
python3 manage.py makemigrations attendance
python3 manage.py migrate
echo 'Create Super User'
python3 manage.py createsuperuser --noinput || echo "Super user already created"
echo 'Collect Static'
python3 manage.py collectstatic --noinput
echo '新增 member.json 資料到資料庫'
python3 manage.py shell < run_impot_data.py
exec "$@"