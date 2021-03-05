# To be used by guardian_patient_pair.py
from django.db import models
from ..models import guardian_patient_pair


class GuardianPatientPairManager(models.Manager):

    def get_patient_mrns_from_guardian(self, guardian_id_: str):
        # Query the database for the patients related to a guardian
        pairs_with_guardian = self.filter(guardian=guardian_id_)

        patient_mrns = []
        for pair in pairs_with_guardian:
            patient_mrns.append(pair.patient_id)
        return patient_mrns

    def get_guardian_ids_from_patients(self, patient_mrn_: int):
        # Query the database for the guardians related to a patient
        pairs_with_patient = self.filter(patient=patient_mrn_)

        guardian_ids = []
        for pair in pairs_with_patient:
            guardian_ids.append(pair.guardian_id)
        return guardian_ids

    def get_pair_id(self, guardian_id_: str, patient_mrn_: str):
        # Query the database using guardian id and patient mrn
        pair = self.get(guardian_id=guardian_id_, patient_id=patient_mrn_)
        return pair.pair_id

    def get_pair_creation_time(self, guardian_id_: str, patient_mrn_: str):
        # Query the database using guardian id and patient mrn and return a time
        pair = self.get(guardian_id=guardian_id_, patient_id=patient_mrn_)
        return pair.date_created
