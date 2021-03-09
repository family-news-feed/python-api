from django.db import models
from ..user_types import user_types
from django.contrib.auth.models import User


class DBUser(models.Model):
    # a profile model attached to a User for extra info
    # https://docs.djangoproject.com/en/3.1/topics/auth/customizing/#custom-permissions
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    access_token = models.CharField(max_length=255)
    refresh_token = models.CharField(max_length=255)
    last_login = models.DateTimeField(auto_now=True)  # last login == 'now' on save
    role = models.CharField(max_length=5, choices=user_types)

