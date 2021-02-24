from django.db import models
from django.core.validators import RegexValidator
from .. import languages_and_countries as lang
from ..managers import patient_manager


class Patient(models.Model):
    medical_record_number = models.BigIntegerField(primary_key=True)
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    # this could be the event type + description we get from FHIR database, else change type
    last_status = models.TextField()
    is_eligible = models.BooleanField(default=True)
    objects = patient_manager.PatientManager()

    def get_mrn(self):
        return self.medical_record_number

    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name

    def get_last_status(self):
        return self.last_status

    def is_patient_eligible(self):
        return self.is_eligible

    def set_first_name(self, new_first_name: str):
        self.first_name = new_first_name
        self.save(update_fields=['first_name'])

    def set_last_name(self, new_last_name: str):
        self.last_name = new_last_name
        self.save(update_fields=['last_name'])

    def set_last_status(self, last_status_: str):
        self.last_status = last_status_
        self.save(update_fields=['last_status'])

    def set_is_eligible(self, is_eligible_: bool):
        self.is_eligible = is_eligible_
        self.save(update_fields=['is_eligible'])
