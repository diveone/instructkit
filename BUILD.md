# DEPLOYMENT

```bash
python3 -m venv venv
pip install -r requirements/prod.txt
# OR
pipenv install -r requirements/prod.txt

python manage.py migrate
python manage.py test instruckit/apps/

```
