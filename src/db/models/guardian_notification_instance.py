from django.db import models
from ..event_types import event_types
from django.core.validators import RegexValidator
from ..managers import guardian_notification_instance_manager


class GuardianNotificationInstance(models.Model):
    notification_id = models.BigAutoField(primary_key=True)
    guardian_patient_pair = models.ForeignKey('GuardianPatientPair', on_delete=models.CASCADE)
    time_sent = models.DateTimeField()
    message = models.TextField()
    event_type = models.CharField(max_length=15, choices=event_types)
    # Taken from https://stackoverflow.com/questions/19130942/whats-the-best-way-to-store-phone-number-in-django-models
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number format must be: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17)  # validators should be a list
    objects = guardian_notification_instance_manager.GuardianNotificationInstanceManager()

    def get_id(self):
        return self.notification_id

    def get_guardian_patient_pair(self):
        return self.guardian_patient_pair

    def get_time_sent(self):
        return self.time_sent

    def get_message(self):
        return self.message

    def get_event_type(self):
        return self.event_type

    def get_phone_number(self):
        return self.phone_number
