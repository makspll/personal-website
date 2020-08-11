from wagtail.documents.views import serve
import requests
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from wagtail.documents.models import Document
import ntpath
from .models import ArticlePage

def view_document(request, document_id, document_filename):
    """
    Calls the normal document `serve` view, except makes it not an attachment.
    """
    # Get response from `serve` first
    requested_doc = Document.objects.get(id=document_id)
    response = serve.serve(request, document_id, ntpath.basename(requested_doc.file.name))
    
    if isinstance(response,HttpResponseRedirect):
        response = requests.get(response.url)
        # we convert to django response from python response, otherwise middleware freaks out
        response = HttpResponse(
            content=response.content,
            status=response.status_code,
            content_type=response.headers['Content-Type']
        )
        response['Content-Disposition'] = 'inline; filename="{0}"'.format(document_filename)
    else:
        # Remove "attachment" from response's Content-Disposition
        response['Content-Disposition'] = 'inline; filename="{0}"'.format(document_filename)
    # Return the response
    return response

