import time
import requests
from .sms_base import SMSBase
from requests.auth import HTTPBasicAuth


class Televox(SMSBase):
    # Ask for username and password, do not commit
    username = ''
    password = ''
    url = 'https://revenuecyclecert.cernerworks.com/edi/sms/submit'

    header = {
        # also don't commit this
        'Authorization': 'Basic {}',
        'Content-Type': 'application/json',
    }

    body_template = {
        'ediRequestAttributes': {
            'transactionType': 'REALTIME'
        },
        'method': 'SMS1',
        'type': 'NOTIFY',
        'realTime': True,
        'countryCode': 1,
        'sendTime': '',
        'shortMessage': {
            'message': '',
            'phoneNumbers': [
            {
                'phoneNumber': ''
            }
            ]
        }
    }

    def build_msg_request(self, message, phone_number):
        payload = self.body_template
        payload['shortMessage']['message'] = message
        payload['shortMessage']['phoneNumbers'][0]['phoneNumber'] = phone_number
        return payload

    def send_msg(self, payload):
        r = requests.request("POST", self.url,  headers=self.header, json=payload, auth=HTTPBasicAuth(self.username, self.password))
        return r.text
