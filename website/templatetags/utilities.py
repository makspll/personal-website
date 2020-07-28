from django import template
import uuid 
import re
from wagtail.core.models import Page 

register = template.Library()

@register.simple_tag
def get_uuid():
    return uuid.uuid4()  

@register.simple_tag
def get_uuid_digits():
    return re.sub(r'\D','',str(uuid.uuid4())) 

@register.simple_tag
def get_page_ancestors_without_root(page):
    if page:
        ancestors_with_root = page.get_ancestors()
        if len(ancestors_with_root) > 0:
            return ancestors_with_root[1:] 
