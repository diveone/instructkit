# DEPLOYMENT

Preparation:
```bash
python3 -m venv venv
pip install -r requirements/prod.txt
# OR
pipenv install -r requirements/prod.txt

python3 manage.py migrate
python3 manage.py test instruckit/apps/

```

## Operations
```
heroku logs --tail

```
__Server__
https://devcenter.heroku.com/articles/python-gunicorn

__Django__
https://devcenter.heroku.com/articles/django-app-configuration
