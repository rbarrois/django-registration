from django.contrib.auth import models as auth_models


class MockUser(auth_models.User):
    """
    This class exists solely for testing purposes
    """

    objects = auth_models.UserManager()
