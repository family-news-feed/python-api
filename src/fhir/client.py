import os
from fhirclient.client import FHIRClient as client

# FHIR Data Access Scopes
scopes = [
    'offline_access',
    'system/Appointment.read',
    'system/CarePlan.read',
    'system/Encounter.read',
    'system/MedicationAdministration.read',
    'system/MedicationOrder.read',
    'system/Observation.read',
    'system/Patient.read',
    'system/Procedure.read',
]

# FHIR Auth Handshake Settings
SETTINGS = {
    'app_id': os.environ.get('DJANGO_FHIR_APP_ID'),
    'api_base': os.environ.get('DJANGO_FHIR_API_BASE'),
    'app_secret': os.environ.get('DJANGO_FHIR_CLIENT_ID'),
    # the parameter is called redirect_uri but it is URL scheme not uri (encoded URL)
    'redirect_uri': os.environ.get('DJANGO_FHIR_REDIRECT_URL'),
    'scope': ' '.join(scopes),
}

class FHIRClient(client):
    ''' Cached connection manager for the FHIR database.
    '''

    def __init__(self, **kwargs):
        save_func = kwargs.get('save_func')
        state = kwargs.get('state')
        if state:
            super().__init__(state=state, save_func=save_func)
        else:
            settings = SETTINGS.copy()
            launch_token = kwargs.get('launch_token')
            if launch_token:
                settings.launch_token = launch_token
            patient_id = kwargs.get('patient_id')
            if patient_id:
                settings.patient_id = patient_id
            super().__init__(settings=settings, save_func=save_func)
