from django.urls import include, path, re_path
from .views import view_document

urlpatterns = [
    re_path(r'^document/view/(\d+)/(.*)$', view_document,name="view_document"),
]