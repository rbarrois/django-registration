VERSION = (0, 8, 0, 'alpha', 1)

def get_version():
    version = '%s.%s' % (VERSION[0], VERSION[1])
    if VERSION[2]:
        version = '%s.%s' % (version, VERSION[2])
    if VERSION[3:] == ('alpha', 0):
        version = '%s pre-alpha' % version
    else:
        if VERSION[3] != 'final':
            version = "%s %s" % (version, VERSION[3])
            if VERSION[4] != 0:
                version = '%s %s' % (version, VERSION[4])
    return version

from django.conf import settings
from django.db import models as django_db_models
from django.contrib.auth import models as auth_models


def get_user_model():
    if hasattr(settings, 'REGISTRATION_USER_MODEL'):
        app_label, model_label = settings.REGISTRATION_USER_MODEL.split('.')
        return django_db_models.get_model(app_label, model_label)
    else:
        return auth_models.User
