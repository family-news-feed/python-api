# To be used by guardian.py
from django.db import models
from datetime import datetime
from ..models import guardian


class GuardianManager(models.Manager):
    # Manager for table-level methods on the Guardian model
    # noinspection PyMethodMayBeStatic
    def create_new_guardian(self, first_name_: str, last_name_: str, phone_number_: str, time_start_: datetime.time,
                            time_end_: datetime.time, pref_lang_: str):
        # Create a new guardian and add to FNF database
        # todo: add arg validation
        new = guardian.Guardian(first_name=first_name_, last_name=last_name_, phone_number=phone_number_,
                                time_start=time_start_, time_end=time_end_, preferred_language=pref_lang_)
        new.save()

    def search_for_guardian_by_number(self, phone_number_: str):
        # Query the database using number
        return self.filter(phone_number=phone_number_)

    def search_for_guardian_by_name(self, first_name_: str, last_name_: str = None):
        # Query the database using number
        queryset = self.filter(first_name__iexact=first_name_)
        if last_name_ is not None:
            queryset = queryset.filter(last_name__iexact=last_name_)
        return queryset
