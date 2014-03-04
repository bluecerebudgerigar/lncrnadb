import os
gettext = lambda s: s
# Django settings for deployment server



PROJECT_PATH = os.path.split(os.path.abspath(os.path.dirname(__file__)))[0]
#PROJECT_PATH = location of the project, where manage.py is at


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.path.join(PROJECT_PATH, 'database.sqlite'),
    }
}


