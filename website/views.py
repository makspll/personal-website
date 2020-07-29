from wagtail.documents.views import serve
import requests
from django.http import HttpResponseRedirect

def view_document(request, document_id, document_filename):
    """
    Calls the normal document `serve` view, except makes it not an attachment.
    """
    # Get response from `serve` first
    response = serve.serve(request, document_id, document_filename)
    
    print( type(response))
    if isinstance(response,HttpResponseRedirect):
        print(11)
        response = requests.get(response.url)
        print(22)
        response.headers['Content-Disposition'] = 'inline; filename="{0}"'.format(document_filename)
        print(33)
    else:
        print(1)
        # Remove "attachment" from response's Content-Disposition
        response['Content-Disposition'] = 'inline; filename="{0}"'.format(document_filename)
        print(2)
    # Return the response
    return response