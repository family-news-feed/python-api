# To be used by guardian_notification_instance.py
from django.db import models
from ..models import guardian_notification_instance


class GuardianNotificationInstanceManager(models.Manager):

    def search_logs_event_type(self, event_type_: str):
        # Query instances and filter by event type
        matching_instances = self.filter(event_type=event_type_)

        return list(matching_instances)

    def search_logs_by_pair_id(self, pair_id_: str):
        # Query instances and filter by pair id
        matching_instances = self.filter(guardian_patient_pair_id=pair_id_)

        return list(matching_instances)

    def search_logs_by_phone(self, phone_: str):
        # Query instances and filter by phone number
        matching_instances = self.filter(phone_number=phone_)

        return list(matching_instances)
