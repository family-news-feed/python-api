from django.http import HttpResponseRedirect, JsonResponse, HttpResponseNotAllowed, HttpResponseServerError
from django.conf import settings
from fhir.client import FHIR
from utils.request import get_query_parameters

def oauth_handshake(request):
    ''' Perform an OAuth 2 authorization handshake with the FHIR Server
    '''

    # Only support GET requests
    if (request.method != 'GET'):
        return HttpResponseNotAllowed(['GET'])

    # extract launch_token, patient_id from query string
    query = get_query_parameters(request)
    launch_token = query.get('launch_token') if 'launch_token' in query else None
    patient_id = query.get('patient_id') if 'patient_id' in query else None

    # initiate connection to FHIR server
    smart = FHIR.get_session(request, launch_token=launch_token, patient_id=patient_id)
    response = {
        'message': 'Authorization failed',
        'status': 500,
    }

    if smart.prepare() and smart.authorize_url is None:
        # do not need to auth
        response.update(message='Authorization success', status=200)
    elif smart.authorize_url is not None:
        # redirect to authorization url
        return HttpResponseRedirect(redirect_to=smart.authorize_url)
    elif smart.ready:
        # ready to call API after fetching the conformance statement with prepare()
        response.update(message='Authorization success', status=200)

    return JsonResponse(response, status=response['status'])

def redirect_callback(request):
    ''' OAuth2 redirect handler
    '''

    # initiate connection to FHIR server
    smart = FHIR.get_session(request)
    response = JsonResponse({
        'message': 'Authorization redirect success',
        'status': 200,
    })

    try:
        smart.handle_callback(request.GET.get('url'))
        # print('this is the registered request in redirect callback: ', str(request.GET))
    except Exception as e:
        response = HttpResponseServerError('Authorization redirect failure')
    return response