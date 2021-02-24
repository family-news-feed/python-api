from rest_framework.serializers import ModelSerializer
from ..models.guardian_notification_instance import GuardianNotificationInstance


class GuardianNotificationInstanceSerializer(ModelSerializer):
    class Meta:
        model = GuardianNotificationInstance
        fields = (
            'notification_id',
            'guardian_patient_pair_id',
            'time_sent',
            'message',
            'event_type',
            'phone_number',
        )