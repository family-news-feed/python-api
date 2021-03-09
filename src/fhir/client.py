import functools
from django.conf import settings
from fhirclient.client import FHIRClient

class FHIR(FHIRClient):
    ''' Cached connection manager for the FHIR database.
    '''

    def __init__(self, session, **kwargs):
        save_func = functools.partial(FHIR._save_fhir_state, session, settings.DJANGO_SESSION_KEY)
        state = session.get(settings.DJANGO_SESSION_KEY)
        if state is not None:
            super().__init__(state=state, save_func=save_func)
        else:
            sett = settings.FHIR_SETTINGS.copy()
            for arg in kwargs:
                sett[arg] = kwargs[arg]
            super().__init__(settings=sett, save_func=save_func)
        self.save_state()

    @staticmethod
    def _save_fhir_state(session, key, state):
        session[key] = state

    @staticmethod
    def get_session(request, **kwargs):
        return FHIR(request.session, **kwargs)

    @staticmethod
    def logout_session(request):
        if request.session is not None and settings.DJANGO_SESSION_KEY in request.session:
            smart = FHIR.get_session(request)
            smart.reset_patient()

    @staticmethod
    def reset_session(request):
        if request.session is not None and settings.DJANGO_SESSION_KEY in request.session:
            del request.session[settings.DJANGO_SESSION_KEY]