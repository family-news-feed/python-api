from django.db import models
from django.core.validators import RegexValidator
from .. import languages_and_countries as lang


class GuardianPatientPair(models.Model):
    pair_id = models.BigAutoField(primary_key=True)
    guardian_id = models.ForeignKey('Guardian', on_delete=models.CASCADE)
    patient_mrn = models.ForeignKey('Patient', on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
