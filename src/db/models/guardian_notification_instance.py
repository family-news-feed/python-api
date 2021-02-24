from django.db import models
from ..event_types import event_types
from django.core.validators import RegexValidator


class GuardianNotificationInstance(models.Model):
    notification_id = models.BigAutoField(primary_key=True)
    guardian_patient_pair_id = models.ForeignKey('GuardianPatientPair', on_delete=models.CASCADE)
    time_sent = models.DateTimeField()
    message = models.TextField()
    event_type = models.CharField(max_length=15, choices=event_types)
    # Taken from https://stackoverflow.com/questions/19130942/whats-the-best-way-to-store-phone-number-in-django-models
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number format must be: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17)  # validators should be a list