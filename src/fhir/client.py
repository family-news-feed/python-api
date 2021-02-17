from fhirclient import client
import os

# FHIR Data Access Scopes
scopes = [
    'system/*.read'
    # 'system/Appointment.read',
    # 'system/CarePlan.read',
    # 'system/Encounter.read',
    # 'system/MedicationAdministration.read',
    # 'system/MedicationOrder.read',
    # 'system/Observation.read',
    # 'system/Patient.read',
    # 'system/Procedure.read',
]

# FHIR Auth Handshake Settings
settings = {
    'app_id': os.environ.get('DJANGO_FHIR_APP_ID'),
    'api_base': os.environ.get('DJANGO_FHIR_API_BASE'),
    'app_secret': os.environ.get('DJANGO_FHIR_CLIENT_ID'),
    'redirect_uri': os.environ.get('DJANGO_FHIR_REDIRECT_URI'),
    'scope': ' '.join(scopes),
}

class FHIRClient:
    ''' Client connection manager for the FHIR database.
    '''

    def __init__(self, launch_token = None, patient_id = None):
        self._settings = settings.copy()
        if launch_token is not None:
            self._settings['launch_token'] = launch_token
        if patient_id is not None:
            self._settings['patient_id'] = patient_id

        self._ready = False
        self._smart = client.FHIRClient(settings=self._settings)

        if self._smart.ready:
            self._ready = True
        else:
            self._smart.prepare()
            self._ready = self._smart.ready
        self.redirect_url = self._smart.authorize_url

    def readyOrRedirect(self):
        return self._ready or self._smart.ready or self._smart.authorize_url

    def reauthorize(self):
        self._ready = self._smart.prepare() or self._smart.reauthorize()

    def smart(self):
        ready = self.readyOrRedirect()
        if type(ready) is bool and ready:
            return self._smart
        else:
            self.reauthorize()
            ready = self.readyOrRedirect()
            return self._smart if type(ready) is bool and ready else None
