from rest_framework.serializers import ModelSerializer
from ..models.patient import Patient


class PatientSerializer(ModelSerializer):
    class Meta:
        model = Patient
        fields = (
            'medical_record_number',
            'first_name',
            'last_name',
            'last_status',
            'is_eligible',
        )