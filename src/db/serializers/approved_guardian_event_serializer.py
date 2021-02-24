from rest_framework.serializers import ModelSerializer
from ..models.approved_guardian_event import ApprovedGuardianEvent


class ApprovedGuardianEventSerializer(ModelSerializer):
    class Meta:
        model = ApprovedGuardianEvent
        fields = (
            'id',
            'guardian',
            'event_type',
        )