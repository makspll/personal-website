  
from django.contrib.sitemaps import Sitemap
# from website.models import 
from wagtail.core.models import Page
from django.urls import reverse
from django.contrib.contenttypes.models import ContentType
from website.models import ArticlePage
from django.db.models import Q
from wagtail.contrib.sitemaps.views import sitemap

class WagtailPageSitemap(Sitemap):
    def __init__(self,dict,priority):
        self.queryset = dict['queryset']
        self.priority = priority
        self.changefreq = dict.get('changefreq',"daily")

    def location(self,item):
        return item.get_url()
    def lastmod(self,item):
        return item.last_published_at or item.latest_revision_created_at
    def priority(self,item):
        return self.priority

    def changefreq(self,item):
        if callable(changefreq):
            return changefreq(item)
        else:
            return changefreq

def get_sitemaps():
    try:
        sitemaps = {
                    'home': WagtailPageSitemap({
                        'queryset': Page.objects.all()}, priority=1),
                }
        return sitemaps
    except:
        return {}