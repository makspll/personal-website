from django.urls import include, path, re_path
from .views import view_document
from .api import api_router

urlpatterns = [
    path('api/v2/', api_router.urls),
    re_path(r'^document/view/(\d+)/(.*)$', view_document,name="view_document"),
]