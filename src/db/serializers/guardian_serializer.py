from rest_framework.serializers import ModelSerializer
from ..models.guardian import Guardian


class GuardianSerializer(ModelSerializer):
    class Meta:
        model = Guardian
        fields = (
            'guardian_id',
            'first_name',
            'last_name',
            'phone_number',
            'time_start',
            'time_end',
            'preferred_language',
        )