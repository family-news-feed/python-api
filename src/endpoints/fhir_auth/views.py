import os
import functools
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, QueryDict
from fhir.client import FHIRClient

__SESSION_KEY__ = os.environ.get('DJANGO_SESSION_KEY')

def _save_fhir_state(session, key, state):
    session[key] = state

def _get_session(session, **kwargs):
    return FHIRClient(**{
        **{
            'save_func': functools.partial(_save_fhir_state, session, __SESSION_KEY__),
            'state': session.get(__SESSION_KEY__),
        },
        **kwargs
    })

def _fhir_logout(request):
    if request.session is not None and __SESSION_KEY__ in request.session:
        smart = _get_session(request.session)
        smart.reset_patient()

def _fhir_reset(request):
    if __SESSION_KEY__ in request.session:
        del request.session[__SESSION_KEY__]



def oauth_handshake(request):
    ''' Perform an OAuth 2 authorization handshake with the FHIR Server
    '''
    launch_token = ''
    patient_id = ''
    data = dict(message='', patient_id='', launch_token='')
    if (request.method == 'GET'):
        if request.body is not None and len(request.body) > 0:
            # convert bytes to string type
            # print('body=', ''.join([*request.body]))
            pass
        qstring = request.META.get('QUERY_STRING', None)
        if qstring is not None and len(qstring) > 0:
            query_params = QueryDict(qstring)
            if 'launch_token' in query_params:
                data.update(launch_token=query_params.get('launch_token', ''))
            if 'patient_id' in query_params:
                data.update(patient_id=query_params.get('patient_id', ''))
    elif (request.method == 'POST'):
        if request.body is not None and len(request.body) > 0:
            # convert bytes to string type
            # print('body=', ''.join([*request.body]))
            pass
        data.update(
            launch_token=request.POST.get('launch_token', ''),
            patient_id=request.POST.get('patient_id', ''),
        )
    data.update(message='Authorization success')
    return JsonResponse(data)

    # launch_token = request.GET.get('launch_token', None)
    # if launch_token:
    #     data.launch_token = launch_token
    # patient_id = request.GET.get('patient_id', None)
    # if patient_id:
    #     data.patient_id = patient_id
    # smart = _get_session(request, launch_token=launch_token, patient_id=patient_id)
    # if (
    #     smart.ready
    #     and smart.patient is not None
    #     and smart.authorize_url is not None
    # ):
    # return JsonResponse({**data, **request.GET})
    # else:
    #     return HttpResponseRedirect(redirect_to=smart.authorize_url)

def redirect_callback(request):
    ''' OAuth2 redirect handler
    '''
    smart = _get_session(request)
    try:
        smart.handle_callback(request.GET.get('url'))
        print('this is the registered request in redirect callback: ', str(request))
    except Exception as e:
        return JsonResponse({
            'message': 'Authorization failure',
            'error_code': 'AUTH_FAIL'
        }, status=503)
    return HttpResponseRedirect(redirect_to='/')