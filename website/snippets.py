from django.db import models
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.core.fields import StreamField
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.core.models import Page
from wagtail.snippets.models import register_snippet
from .blocks import ExternalLinkWithChildrenBlock, PageLinkWithChildrenBlock, SocialMediaLinkBlock

class Navbar(models.Model):
    """
    Model that represents website navigation bars.  Can be modified through the
    snippets UI. 
    """
    name = models.CharField(max_length=255)
    menu_items = StreamField([
        ('external_link', ExternalLinkWithChildrenBlock()),
        ('page_link', PageLinkWithChildrenBlock()),
        ],)

    panels = [
        FieldPanel('name'),
        StreamFieldPanel('menu_items')
    ]

    def __str__(self):
        return self.name

register_snippet(Navbar)


class Footer(models.Model):
    name = models.CharField(max_length=255)
    social_items = StreamField([
        ('social_link',SocialMediaLinkBlock()),
    ],)

    panels = [
        FieldPanel('name'),
        StreamFieldPanel('social_items'),
    ]

    def __str__(self):
        return self.name

register_snippet(Footer)


class Header(models.Model):
    """
    Represents the header of a page, designed to be placed under the navbar
    """

    name = models.CharField(max_length=255)
    background_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )

    heading = models.CharField(max_length=255)
    lead_paragraph = models.CharField(max_length=255)

    fill_view_height = models.BooleanField(default=True)
    include_slide_down_sign = models.BooleanField(default=False)
    slide_down_text = models.CharField(max_length=255,default="Slide Down")
    
    panels = [
        FieldPanel("name"),
        ImageChooserPanel("background_image"),
        FieldPanel("heading"),
        FieldPanel("lead_paragraph"),
        FieldPanel("fill_view_height"),
        FieldPanel("include_slide_down_sign"),
        FieldPanel("slide_down_text"),
    ]

    def __str__(self):
        return self.name

register_snippet(Header)