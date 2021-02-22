# To be used by guardian.py
from django.db import models
from datetime import datetime
from ..models import guardian


class GuardianManager(models.Manager):
    def get_guardian_by_number(self, phone_number_: str):
        # Query the database using number
        # Number is primary key, always one instance
        return self.get(phone_number=phone_number_)

    def get_guardian_by_id(self, guardian_id_: str):
        # Query the database using id
        # Id is primary key, always one instance
        return self.get(guardian_id=guardian_id_)

    def search_for_guardians_by_name(self, first_name_: str, last_name_: str = None):
        # Query the database using name
        queryset = self.filter(first_name__iexact=first_name_)
        if last_name_ is not None:
            queryset = queryset.filter(last_name__iexact=last_name_)
        return list(queryset)
