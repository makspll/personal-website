"""personal_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, re_path, include

from wagtail.admin import urls as wagtailadmin_urls
from wagtail.core import urls as wagtail_urls
from wagtail.documents import urls as wagtaildocs_urls

from django.http import HttpResponse
from django.template import loader

from website import urls as website_urls
from tz_detect import urls as tz_urls
from wagtail.contrib.sitemaps.views import sitemap
from .api import api_router

## allow settings to add env dependent patterns
try:
    url_additional_patterns = settings.DEFAULT_URL_PATTERNS
except:
    url_additional_patterns = []
urlpatterns = url_additional_patterns + [
    path('sitemap.xml/',sitemap),
    path('robots.txt/', include('robots.urls')),
    path('tz_detect/', include(tz_urls)),
    path('admin/', admin.site.urls),
    path('api/v2/', api_router.urls),
    path('cms/',include(wagtailadmin_urls)),
    path('documents/',include(wagtaildocs_urls)),
    path('',include(wagtail_urls)),
    path('',include(website_urls)),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT) 
