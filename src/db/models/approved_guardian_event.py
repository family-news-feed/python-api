from django.db import models
from ..event_types import event_types
from ..managers import approved_guardian_event_manager

class ApprovedGuardianEvent(models.Model):
    id = models.BigAutoField(primary_key=True)
    guardian = models.ForeignKey('Guardian', on_delete=models.CASCADE)
    event_type = models.CharField(max_length=15, choices=event_types)
    objects = approved_guardian_event_manager.ApprovedGuardianEventManager()
