from django.db import models
from ..event_types import event_types
from ..managers import approved_patient_event_manager

class ApprovedPatientEvent(models.Model):
    id = models.BigAutoField(primary_key=True)
    patient = models.ForeignKey('Patient', on_delete=models.CASCADE)
    event_type = models.CharField(max_length=15, choices=event_types)
    objects = approved_patient_event_manager.ApprovedPatientEventManager()
