from wagtail.core import blocks
from django.db import models
from django.utils.functional import cached_property

class BaseLinkBlock(blocks.StructBlock):
    """
    Base StructBlock class used to prevent DRY code.
    """
    display_text = blocks.CharBlock(required=False)
    fa_icon_class = blocks.CharBlock(required=False)

class ExternalLinkBlock(BaseLinkBlock):
    """
    Block that holds a link to any URL.
    """
    link = blocks.URLBlock()

    class Meta:
        template = 'website/blocks/nav_links/external_link_block.html'

class PageLinkBlock(BaseLinkBlock):
    """
    Block that holds a page.
    """
    page = blocks.PageChooserBlock()

    class Meta:
        template = 'website/blocks/nav_links/page_link_block.html'

class LinkChildrenBlock(blocks.StructBlock):
    """
    Base childblock for second level children.
    """
    children = blocks.StreamBlock(
            [
                ('external_link', ExternalLinkBlock()),
                ('page_link', PageLinkBlock()),
            ]
        ,required=False)

class ExternalLinkWithChildrenBlock(LinkChildrenBlock, ExternalLinkBlock):
    """
    Uses LinkChildrenBlock as a mixin to create an ExternalLinkBlock that supports Children.
    """
    pass

class PageLinkWithChildrenBlock(LinkChildrenBlock, PageLinkBlock):
    """
    Uses LinkChildrenBlock as a mixin to create a PageLinkBlock that supports Children.
    """
    pass



class SocialMediaLinkBlock(blocks.StructBlock):

    link = blocks.URLBlock()
    social_type = blocks.ChoiceBlock(choices=[
        ("fb","facebook"),
        ("tt","twitter"),
        ("li","linked-in"),
        ("gh","github"),
    ])

    class Meta:
        template = 'website/blocks/social_media/social_link_block.html'

from wagtail.documents.blocks import DocumentChooserBlock
    
class BaseDocumentEmbeddBlock(blocks.StructBlock):
    title = blocks.CharBlock(max_length=255,default="Document")
    description = blocks.CharBlock(max_length=255,default="Example description")
    document = DocumentChooserBlock()

class PDFEmbeddBlock(BaseDocumentEmbeddBlock): 
    """
        Block designed to embedd pdf content and degrade nicely with browser incompatibilities
    """
    class Meta:
        template = 'website/blocks/documents/pdf_block.html'


class BaseStoryBlock(blocks.StructBlock):
    pass

class TimelineEventBlock(blocks.StructBlock):
    date = blocks.DateBlock(required=False)
    header = blocks.CharBlock(max_length=255,required=False)
    lead_paragraph = blocks.RichTextBlock(required=False)

    class Meta:
        template = "website/blocks/stories/timeline_event_block.html"

class TimelineBlock(BaseStoryBlock):
    timeline_items = blocks.StreamBlock([
        ("event",TimelineEventBlock())
    ])

    class Meta:
        template = "website/blocks/stories/timeline_block.html"

class ProjectBlock(blocks.StructBlock):
    override_title = blocks.CharBlock(required=False)
    project_page = blocks.PageChooserBlock(page_type="website.ProjectArticlePage")

    class Meta:
        template = "website/blocks/projects/project_block.html"

class ProjectListingBlock(blocks.StructBlock):

    heading = blocks.CharBlock(default="Recent Projects", required=False)
    project_items = blocks.ListBlock(ProjectBlock())

    class Meta:
        template = "website/blocks/projects/project_listing_block.html"


from wagtail.images.blocks import ImageChooserBlock




class LinkCardBlock(blocks.StructBlock):
    miniature_image = ImageChooserBlock(required=False)
    linked_page = blocks.PageChooserBlock()
    heading = blocks.CharBlock(max_length=255)
    text = blocks.CharBlock(max_length=255)
    link_text = blocks.CharBlock(max_length=255)

class LinkCardsBlock(blocks.StructBlock):
    
    link_cards = blocks.ListBlock(LinkCardBlock())


    
class AwardBlock(blocks.StructBlock):
    name = blocks.CharBlock(max_length=255)
    description = blocks.CharBlock(max_length=1024)
    award_value = blocks.ChoiceBlock(choices=[
        ('gold','Gold'),
        ('silver','Silver'),
        ('bronze','Bronze'),
    ])

