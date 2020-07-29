from wagtail.documents.views import serve
import requests


def view_document(request, document_id, document_filename):
    """
    Calls the normal document `serve` view, except makes it not an attachment.
    """
    # Get response from `serve` first
    response = serve.serve(request, document_id, document_filename)

    redirect_url = response.get("Location")
    
    if redirect_url:
        response = requests.get(redirect_url)

    # Remove "attachment" from response's Content-Disposition
    contdisp = response.get('Content-Disposition',"")
    response['Content-Disposition'] = 'inline; filename="{0}"'.format(document_filename)
    # Return the response
    return response