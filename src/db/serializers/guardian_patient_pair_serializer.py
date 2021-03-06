from rest_framework.serializers import ModelSerializer
from ..models.guardian_patient_pair import GuardianPatientPair


class GuardianPatientPairSerializer(ModelSerializer):
    class Meta:
        model = GuardianPatientPair
        fields = (
            'pair_id',
            'guardian',
            'patient',
            'date_created',
        )