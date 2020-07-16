from django.db import models
from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel, InlinePanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.search import index
from wagtail.core.fields import RichTextField

# Create your models here.

class testPage(Page):
    body = RichTextField()
    content_panels = Page.content_panels + [
        FieldPanel("body")
    ]