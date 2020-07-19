from django.db import models
from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel, InlinePanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.snippets.edit_handlers import SnippetChooserPanel
from wagtail.search import index
from wagtail.core.fields import RichTextField
from .snippets import Navbar, Footer
from wagtailmetadata.models import MetadataPageMixin

# Create your models here.

class testPage(Page):
    body = RichTextField()
    content_panels = Page.content_panels + [
        FieldPanel("body")
    ]

class websitePage(MetadataPageMixin,Page):
    template = "website/pages/website_page.html"
    navbar = models.ForeignKey(
        Navbar,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )

    footer= models.ForeignKey(
        Footer,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )

    content_panels = Page.content_panels + [
        SnippetChooserPanel("navbar"),
        SnippetChooserPanel("footer")
    ]
