# DEPLOYMENT

## Deployment Checklist

Always check the build locally before any deployment. 

```bash
python3 -m venv venv
pip install -r requirements/beta.txt
# OR
pipenv install

python3 manage.py migrate
python3 manage.py test instruckit/apps/
```


## Heroku

Heroku has it's own settings file. It's the testing server for running incremental changes.

- [Heroku Gunicorn Docs](https://devcenter.heroku.com/articles/python-gunicorn)
- [Heroku Django Docs](https://devcenter.heroku.com/articles/django-app-configuration)

Heroku only requires:

- Environment variable setup on the dashboard
- Django-heroku package

It auto-configures: database, logging, static and testing. Finally: 

```bash
git push heroku master
heroku logs --tail

# Server operations
heroku run python3 manage.py demo  # seed initial data
heroku run python3 manage.py createsuperuser  # create a test user
```


## Troubleshooting

### Reset Database

Go to Heroku dashboard to reset the database. You can't do it from `heroku run` unless the app is managing it's own database.

### Server Errors with No Logs

Turn on `DEBUG=True` in settings to see the full Heroku output when getting any errors, especially 500 errors. Then redeploy the the change as a Hotfix. Amend commits until issue is fixed.
