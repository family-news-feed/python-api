from django.db import models
from django.contrib.auth.hashers import make_password
from ..user_types import user_types


class DBUser(models.Model):
    username = models.CharField(primary_key=True, max_length=256)
    access_token = models.CharField(max_length=255)
    refresh_token = models.CharField(max_length=255)
    last_login = models.DateTimeField(auto_now=True)  # last login == 'now' on save
    role = models.CharField(max_length=5, choices=user_types)

    def save(self, *args, **kwargs):
        self.username = make_password(self.username) # hash username on save
        super().save(*args, **kwargs)  # Call the "real" save() method.
