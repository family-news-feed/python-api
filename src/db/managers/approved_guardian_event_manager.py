# To be used by guardian_notification_instance.py
from django.db import models
from ..models import approved_guardian_event


class ApprovedGuardianEventManager(models.Manager):

    def get_guardian_approved_events(self, guardian_id_: str):
        # Query the database for the events related to a guardian
        events_with_guardians = self.filter(guardian=guardian_id_)

        approved_events = []
        for entry in events_with_guardians:
            approved_events.append(entry.event_type)
        return approved_events

    def remove_guardian_approved_event(self, guardian_id_: str, event_type_: str):
        # Query the database for the event and guardian and delete the row
        row = self.filter(guardian=guardian_id_, event_type=event_type_)
        row.delete()
