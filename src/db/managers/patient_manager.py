from django.db import models


class PatientManager(models.Manager):
    def get_patient_by_mrn(self, mrn: str):
        # Query the database using id
        # MRN is primary key, always one instance
        return self.get(medical_record_number=mrn)

    def search_for_patients_by_name(self, first_name_: str, last_name_: str = None):
        # Query the database using name
        queryset = self.filter(first_name__iexact=first_name_)
        if last_name_ is not None:
            queryset = queryset.filter(last_name__iexact=last_name_)
        return list(queryset)

    def all_eligible_patients(self):
        return list(self.filter(is_eligible=True))
