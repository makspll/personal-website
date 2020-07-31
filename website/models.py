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
from .blocks import PDFEmbeddBlock, TimelineBlock, ProjectListingBlock
from datetime import date
from wagtail.core.blocks import RichTextBlock, RawHTMLBlock
from wagtail.core.fields import StreamField
from wagtailcodeblock.blocks import CodeBlock

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


class FreeformContentMixin(models.Model):

    freeform_items = StreamField([
        ("pdf",PDFEmbeddBlock()),
        ("timeline",TimelineBlock()),
        ("code",CodeBlock()),
        ("projects",ProjectListingBlock()),
        ("text",RichTextBlock())
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



class ArticlePageMixin(models.Model):
    
    short_title = models.CharField(max_length=255,default="Article")

    featured_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )

    blurb = RichTextField(features=[
            'bold','italic','ol','ul','hr','link','document-link'
        ])

    article_items = StreamField([
        ("text",RichTextBlock()),
        ("code", CodeBlock()),
        ("html",RawHTMLBlock()),
    ],null=True,blank=True)

        
    show_in_listings = models.BooleanField(default=True)

    content_panels = [
        FieldPanel("short_title"),
        ImageChooserPanel("featured_image"),
        FieldPanel("blurb"),
        StreamFieldPanel("article_items"),
        FieldPanel("show_in_listings"),
    ]

    class Meta:
        abstract = True

from modelcluster.fields import ParentalKey
from modelcluster.contrib.taggit import ClusterTaggableManager
from taggit.models import TaggedItemBase

class ArticlePageTag(TaggedItemBase):
    content_object = ParentalKey('website.ArticlePage', related_name='tagged_items')

class ArticlePage(MetadataPageMixin,
                    Page,
                    NavigationPageMixin,
                    ArticlePageMixin,):

    parent_page_types = ["website.ArticleListingPage"]

    template = "website/pages/article_page.html"

    tags = ClusterTaggableManager(through=ArticlePageTag, blank=True)

    content_panels = \
        NavigationPageMixin.content_panels +\
        Page.content_panels +\
        ArticlePageMixin.content_panels + [
            FieldPanel("tags"),
        ]

class ProjectArticlePage(ArticlePage):
    template = "website/pages/project_article_page.html"
    

    project_start_date = models.DateField(blank=True,null=True,default=date.today)
    project_end_date = models.DateField(blank=True,null=True,default=date.today)
    
    content_panels = ArticlePage.content_panels + [
        FieldPanel("project_start_date"),
        FieldPanel("project_end_date"),
    ]

class ArticleListingPage(MetadataPageMixin,
                            Page,
                            HeaderedPageMixin,
                            NavigationPageMixin):
    template = "website/pages/article_listing_page.html"

    def get_context(self,request):
        context = super().get_context(request)

        children = self.get_descendants().order_by('-first_published_at').specific()

        context['articles'] = children 

        return context

    content_panels = Page.content_panels +HeaderedPageMixin.content_panels + NavigationPageMixin.content_panels + [
    ]
