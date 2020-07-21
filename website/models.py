from django.db import models
from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel, InlinePanel, StreamFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.snippets.edit_handlers import SnippetChooserPanel
from wagtail.documents.edit_handlers import DocumentChooserPanel
from wagtail.search import index
from wagtail.core.fields import RichTextField
from .snippets import Navbar, Footer, Header
from wagtailmetadata.models import MetadataPageMixin
from .blocks import PDFEmbeddBlock, TimelineBlock
# Create your models here.


class NavigationPageMixin(models.Model):
    navbar = models.ForeignKey(
        Navbar,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )

    footer = models.ForeignKey(
        Footer,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )

    content_panels = [
        SnippetChooserPanel("navbar"),
        SnippetChooserPanel("footer")
    ]

    class Meta:
        abstract = True



class HeaderedPageMixin(models.Model):    
    header = models.ForeignKey(
        Header,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )

    content_panels = [
        SnippetChooserPanel("header")
    ]

    class Meta:
        abstract = True

from wagtail.core.fields import StreamField

class FreeformContentMixin(models.Model):

    freeform_items = StreamField([
        ("pdf",PDFEmbeddBlock()),
        ("timeline",TimelineBlock()),
    ],null=True,blank=True)

    content_panels = [
        StreamFieldPanel("freeform_items"),
    ]

    class Meta:
        abstract = True

class FreeformPage(MetadataPageMixin,
                    Page,
                    HeaderedPageMixin,
                    NavigationPageMixin,
                    FreeformContentMixin):

    template = "website/pages/freeform_page.html"

    content_panels = \
        NavigationPageMixin.content_panels +\
        HeaderedPageMixin.content_panels +\
        Page.content_panels +\
        FreeformContentMixin.content_panels

