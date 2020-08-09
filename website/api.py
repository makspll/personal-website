from wagtail.api.v2.views import PagesAPIViewSet
from wagtail.api.v2.router import WagtailAPIRouter
from wagtail.images.api.v2.views import ImagesAPIViewSet
from wagtail.documents.api.v2.views import DocumentsAPIViewSet
from rest_framework import serializers
from rest_framework import viewsets
from .models import ArticlePage, ProjectArticlePage
from rest_framework import generics
from taggit.models import Tag
from django.contrib.contenttypes.models import ContentType  

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model= Tag
        fields=['name']

class ProjectTagListView(generics.ListAPIView):
    serializer_class = TagSerializer
    def get_queryset(self):
        return Tag.objects.filter( 
                articlepage__content_type=ContentType.objects.get_for_model(ProjectArticlePage)
            ).order_by('name')
        

# Create the router. "wagtailapi" is the URL namespace
api_router = WagtailAPIRouter('wagtailapi')

# Add the three endpoints using the "register_endpoint" method.
# The first parameter is the name of the endpoint (eg. pages, images). This
# is used in the URL of the endpoint
# The second parameter is the endpoint class that handles the requests
api_router.register_endpoint('pages', PagesAPIViewSet)
api_router.register_endpoint('images', ImagesAPIViewSet)
api_router.register_endpoint('documents', DocumentsAPIViewSet)
