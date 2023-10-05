#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requirements.txt
pip install google-api-python-client
pip install google_auth_oauthlib

python manage.py collectstatic --no-input
python manage.py migrate
python manage.py superuser


