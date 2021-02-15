from django.db import models
from django.core.validators import RegexValidator
from .. import languages_and_countries as lang


class Patient(models.Model):
    medical_record_number = models.BigIntegerField(primary_key=True)
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    # Taken from https://stackoverflow.com/questions/19130942/whats-the-best-way-to-store-phone-number-in-django-models
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number format must be: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17)  # validators should be a list
    # this could be the event type + description we get from FHIR database, else change type
    last_status = models.TextField()
    is_eligible = models.BooleanField(default=True)
