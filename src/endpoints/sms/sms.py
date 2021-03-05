from rest_framework import decorators, authentication, response
from ..sms.vendors.televox import Televox

sms_vendor = Televox()

@decorators.api_view(['POST'])
@decorators.authentication_classes([authentication.BasicAuthentication])
def send_sms(request):
    message = request.data['message']
    phone = request.data['phone_number']
    payload = sms_vendor.build_msg_request(message, phone)
    s = sms_vendor.send_msg(payload)
    return response.Response(s)