from django import template
import uuid 
import re

register = template.Library()

@register.simple_tag
def get_uuid():
    return uuid.uuid4()  

@register.simple_tag
def get_uuid_digits():
    return re.sub('\D','',str(uuid.uuid4())) 