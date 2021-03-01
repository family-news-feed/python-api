from django.db import models
from django.core.validators import RegexValidator
from .. import languages_and_countries as lang
import uuid
from ..managers import guardian_manager
import datetime


class Guardian(models.Model):
    # can be changed depending on how we ID guardians
    guardian_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    # Taken from https://stackoverflow.com/questions/19130942/whats-the-best-way-to-store-phone-number-in-django-models
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number format must be: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, unique=True)  # validators should be a list
    time_start = models.TimeField(default=datetime.time(hour=8))
    time_end = models.TimeField(default=datetime.time(hour=22))
    preferred_language = models.CharField(max_length=2, choices=lang.languages, default='en')
    objects = guardian_manager.GuardianManager()

    def __str__(self):
        return self.first_name + " " + self.last_name + " (" + str(self.guardian_id) + ")"

    def get_id(self):
        return self.guardian_id

    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name

    def get_phone_number(self):
        return self.phone_number

    def get_time_start(self):
        return self.time_start

    def get_time_end(self):
        return self.time_end

    def get_preferred_language(self):
        # returns a tuple of the ISO format and human-readable format (ex. ( 'en', 'English')
        pair = (self.preferred_language, self.get_preferred_language_display())
        return pair

    def set_first_name(self, new_first_name: str):
        self.first_name = new_first_name
        self.save(update_fields=['first_name'])

    def set_last_name(self, new_last_name: str):
        self.last_name = new_last_name
        self.save(update_fields=['last_name'])

    def set_phone_number(self, new_phone_number: str):
        # phone number format is '+999999999'
        self.phone_number = new_phone_number
        self.save(update_fields=['phone_number'])

    def set_time_start(self, new_time_start: datetime.time):
        self.time_start = new_time_start
        self.save(update_fields=['time_start'])

    def set_time_end(self, new_time_end: datetime.time):
        self.time_end = new_time_end
        self.save(update_fields=['time_end'])

    def set_preferred_language(self, new_lang_iso: str):
        # use iso language codes
        if new_lang_iso in lang.languages:
            self.preferred_language = new_lang_iso
        self.save(update_fields=['preferred_language'])
