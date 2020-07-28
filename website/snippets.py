from django.db import models
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel, MultiFieldPanel
from wagtail.core.fields import StreamField
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.core.models import Page, Site
from wagtail.snippets.models import register_snippet
from .blocks import ExternalLinkWithChildrenBlock, PageLinkWithChildrenBlock, SocialMediaLinkBlock
import json

class Navbar(models.Model):
    """
    Model that represents website navigation bars.  Can be modified through the
    snippets UI. 
    """
    name = models.CharField(max_length=255)

    generate_items_on_next_save = models.BooleanField(default=False,help_text="override menu_items below and find links automatically using the include in navigation page option when you next click 'save'")
    
    menu_items = StreamField([
        ('external_link', ExternalLinkWithChildrenBlock()),
        ('page_link', PageLinkWithChildrenBlock()),
        ],null=True,blank=True)

    panels = [
        FieldPanel('name'),
        MultiFieldPanel([
            FieldPanel('generate_items_on_next_save',heading="Menu Items"),
            StreamFieldPanel('menu_items'),
        ])

    ]

    def save(self,*args,**kwargs):
        if self.generate_items_on_next_save:
            menu_items = []

            default_site = Site.objects.all().get(is_default_site=True)
            root = default_site.root_page
            #include root page in navigation
            first_level = list(root.get_children()) + [root]
    
            for page in first_level:
                if page == root:
                    child_pages = []
                else:
                    child_pages = page.get_children().in_menu()

                child_items = [{"type":"page_link",
                                "value":{
                                    "display_text": x.title,
                                    "fa_icon_class":"",
                                    "page":x.pk,
                                },
                                } for x in child_pages]

                menu_items.append({
                    "type":"page_link",
                    "value":{
                        "display_text":page.title,
                        "fa_icon_class":"",
                        "page":page.pk,
                        "children":child_items
                        }
                    })
            
            raw_json = json.dumps(menu_items)
            self.generate_items_on_next_save = False
            self.menu_items = raw_json

        return super().save(*args,**kwargs)

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