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

## Troubleshooting

Turn on `DEBUG=True` in settings to see the full Heroku output when getting any errors, especially 500 errors.

Then redeploy the the change as a Hotfix. Amend commits until issue is fixed.
```
heroku logs --tail

```
__Server__
https://devcenter.heroku.com/articles/python-gunicorn

__Django__
https://devcenter.heroku.com/articles/django-app-configuration
