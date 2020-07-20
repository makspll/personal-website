from wagtail.core import blocks



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

from wagtail_blocks.blocks import HeaderBlock, ListBlock, ImageTextOverlayBlock, CroppedImagesWithTextBlock, \
    ListWithImagesBlock, ThumbnailGalleryBlock, ChartBlock, MapBlock, ImageSliderBlock




class BaseStoryBlock(blocks.StructBlock):
    title = blocks.CharBlock(max_length=255,required=False)

class VerticalStoryContentBlock(BaseStoryBlock):
    items = blocks.StreamBlock(
        [
        ('header', HeaderBlock()),
        ('list', ListBlock()),
        ('image_text_overlay', ImageTextOverlayBlock()),
        ('cropped_images_with_text', CroppedImagesWithTextBlock()),
        ('list_with_images', ListWithImagesBlock()),
        ('thumbnail_gallery', ThumbnailGalleryBlock()),
        ('chart', ChartBlock()),
        ('map', MapBlock()),
        ('image_slider', ImageSliderBlock()),
        ('rich_text',blocks.RichTextBlock()),
        ('html',blocks.RawHTMLBlock())])

    class Meta:
        template = 'website/blocks/story/vertical_story_content_block.html'