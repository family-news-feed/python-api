from django.http import QueryDict
from django.conf import settings

def get_query_parameters(request):
    ''' Transform a request's query_string string parameters into a dict.
    '''
    query_string = request.META.get('QUERY_STRING', None)
    return QueryDict(
        query_string if query_string is not None and len(query_string) > 0 else None,
        False,
        settings.DEFAULT_CHARSET
    )
