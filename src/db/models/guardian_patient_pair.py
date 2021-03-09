from django.db import models
from django.core.validators import RegexValidator
from ..managers import guardian_patient_pair_manager


class GuardianPatientPair(models.Model):
    pair_id = models.BigAutoField(primary_key=True)
    guardian = models.ForeignKey('Guardian', on_delete=models.CASCADE)
    patient = models.ForeignKey('Patient', on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    objects = guardian_patient_pair_manager.GuardianPatientPairManager()

    def get_id(self):
        return self.pair_id

    def get_guardian_id(self):
        return self.guardian

    def get_patient_mrn(self):
        return self.patient

    def get_date_created(self):
        return self.date_created
