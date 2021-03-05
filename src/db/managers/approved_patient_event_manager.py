# To be used by patient_notification_instance.py
from django.db import models
from ..models import approved_patient_event


class ApprovedPatientEventManager(models.Manager):

    def get_patient_approved_events(self, patient_mrn_: str):
        # Query the database for the events related to a patient
        events_with_patients = self.filter(patient=patient_mrn_)

        approved_events = []
        for entry in events_with_patients:
            approved_events.append(entry.event_type)
        return approved_events

    def remove_patient_approved_event(self, patient_mrn_: str, event_type_: str):
        # Query the database for the event and patient and delete the row
        row = self.filter(patient=patient_mrn_, event_type=event_type_)
        row.delete()
