from wagtail.documents.views import serve


def view_document(request, document_id, document_filename):
    """
    Calls the normal document `serve` view, except makes it not an attachment.
    """
    # Get response from `serve` first
    response = serve.serve(request, document_id, document_filename)

    # Remove "attachment" from response's Content-Disposition
    contdisp = response.get('Content-Disposition',"")
    response['Content-Disposition'] = 'inline; filename="{0}"'.format(document_filename)
    # Return the response
    return response