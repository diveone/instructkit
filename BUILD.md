# DEPLOYMENT

```bash
virtualenv venv

pip install -r requirements/prod.txt
# OR
pipenv install -r requirements/prod.txt

python manage.py migrate

```