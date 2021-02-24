from rest_framework.serializers import ModelSerializer
from ..models.approved_patient_event import ApprovedPatientEvent


class ApprovedPatientEventSerializer(ModelSerializer):
    class Meta:
        model = ApprovedPatientEvent
        fields = (
            'id',
            'patient_mrn',
            'event_type',
        )