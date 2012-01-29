DATABASES={
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
    }
}

INSTALLED_APPS=[
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'registration_tests',
    'registration',
]

SITE_ID = 1

#REGISTRATION_USER_MODEL = 'registration_tests.MockUser'

ROOT_URLCONF = 'registration_tests.urls'
