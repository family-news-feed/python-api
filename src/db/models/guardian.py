from django.db import models
from django.core.validators import RegexValidator
from .. import languages_and_countries as lang
import uuid


class Guardian(models.Model):
    # can be changed depending on how we ID guardians
    guardian_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    # Taken from https://stackoverflow.com/questions/19130942/whats-the-best-way-to-store-phone-number-in-django-models
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number format must be: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, unique=True)  # validators should be a list
    time_start = models.TimeField()
    time_end = models.TimeField()
    LANGUAGE_CODES = [
        (language[0], language[1]) for language in lang.languages
    ]
    preferred_language = models.CharField(max_length=2, choices=LANGUAGE_CODES)

