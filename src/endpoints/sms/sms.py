from rest_framework import decorators, authentication, response
from ..sms.vendors.televox import Televox
from db.models import *
from .message_builder import MessageBuilder


sms_vendor = Televox()
MB = MessageBuilder()


@decorators.api_view(['POST'])
@decorators.authentication_classes([authentication.BasicAuthentication])
def receive_and_send_update(request):
    patient = request.data['mrn']
    guardian_ids = GuardianPatientPair.objects.get_guardian_ids_from_patients(patient_mrn_=patient)
    event_type = request.data['event_type']
    #todo: check for time restrictions and approved events first, then reference correct message build
    msg = MB.careteam_message("Jane Doe", "RN") #placeholder

    responses = []
    for guardian_id in guardian_ids:
        guardian = Guardian.objects.get_guardian_by_id(guardian_id)
        phone = guardian.get_phone_number().strip("+")
        payload = sms_vendor.build_msg_request(msg, phone)
        s = sms_vendor.send_msg(payload)
        responses.append(s)
    return response.Response(responses)