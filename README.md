# Django Restful API Sample Template Project
This is sample project for restful API server with the Django web framework.

## Set up
- Create project directory and install python packages

    ```
    mkdir sample
    cd sample
    virtualenv -p python3 .venv
    . .venv/bin/activate
    pip install django==1.9.5
    pip install djangorestframework==3.3.3
    pip install django-oauth2-provider
    git clone git@github.com:iandmyhand/DjangoRestAPISampleProject.git
    cd DjangoRestAPISampleProject
    python manage.py makemigrations --settings=www.settings.test ping
    python manage.py test ping
    python manage.py runserver 0.0.0.0:8000
    ```
