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
from .blocks import LinkCardsBlock,PDFEmbeddBlock, TimelineBlock, ProjectListingBlock
from datetime import date
from wagtail.core.blocks import RichTextBlock, RawHTMLBlock
from wagtail.core.fields import StreamField
from wagtailcodeblock.blocks import CodeBlock
from wagtail.api import APIField
from wagtail.images.api.fields import ImageRenditionField
from rest_framework.fields import Field
from wagtail.search import index

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
        ("text",RichTextBlock()),
        ("link_cards",LinkCardsBlock())
    ],null=True,blank=True)

    content_panels = [
        StreamFieldPanel("freeform_items"),
    ]

    api_fields = [
        APIField("freeform_items"),
    ]

    search_fields = [
        index.SearchField('freeform_items'),
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

    api_fields = FreeformContentMixin.api_fields + [

    ]

    search_fields = Page.search_fields + FreeformContentMixin.search_fields + [

    ]

class ArticlePageMixin(models.Model):
    
    short_title = models.CharField(max_length=255,default="Article")

    featured_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )

    tag_line = models.CharField(max_length=255,default="Describe your article in a few words")
    blurb = RichTextField(features=[
            'bold','italic','ol','ul','hr','link','document-link'
        ],default="introduce your article")

    article_items = StreamField([
        ("text",RichTextBlock()),
        ("code", CodeBlock()),
        ("html",RawHTMLBlock()),
    ],null=True,blank=True)

        
    show_in_listings = models.BooleanField(default=True)

    content_panels = [
        FieldPanel("tag_line"),
        FieldPanel("short_title"),
        ImageChooserPanel("featured_image"),
        FieldPanel("blurb"),
        StreamFieldPanel("article_items"),
        FieldPanel("show_in_listings"),
    ]

    api_fields = [
        APIField('tag_line'),
        APIField('short_title'),
        APIField('featured_image'),
        APIField('featured_image_original',serializer=ImageRenditionField('original',source='featured_image')),
        APIField('featured_image_small',serializer=ImageRenditionField('max-700x500',source='featured_image')),
        APIField('featured_image_placeholder',serializer=ImageRenditionField('scale-25', source='featured_image')),
        APIField('featured_image_thumbnail',serializer=ImageRenditionField('fill-250x250-c100', source='featured_image')),
        APIField('blurb'),
        APIField('article_items'),
        APIField('show_in_listings'),

    ]

    search_fields = [
        index.SearchField("short_title",partial_match=True,boost=1.5),
        index.SearchField("tag_line",partial_match=True,boost=1.5),
        index.SearchField("blurb",partial_match=True,boost=1.4),
        index.SearchField("article_items",partial_match=True),
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
    
    def get_context(self,request):
        context = super().get_context(request)

        tag_names =  ' '.join(ArticlePageTag.objects.distinct().values_list('tag__name',flat=True))
        proposed_articles = ArticlePage.objects.live().search(tag_names,operator="or")

        context['relevant_articles'] = proposed_articles 

        return context

    content_panels = \
        NavigationPageMixin.content_panels +\
        Page.content_panels +\
        ArticlePageMixin.content_panels + [
            FieldPanel("tags"),
        ]
    api_fields = ArticlePageMixin.api_fields + [
        APIField("tags")
    ]
    search_fields = Page.search_fields + ArticlePageMixin.search_fields + [
        index.RelatedFields('tags', [
            index.SearchField('name', partial_match=True, boost=5),
        ]),
    ]
    

class ProjectArticlePage(ArticlePage):
    template = "website/pages/project_article_page.html"
    

    project_start_date = models.DateField(blank=True,null=True,default=date.today)
    project_end_date = models.DateField(blank=True,null=True,default=date.today)
    
    content_panels = ArticlePage.content_panels + [
        FieldPanel("project_start_date"),
        FieldPanel("project_end_date"),
    ]

    api_fields = ArticlePage.api_fields + [
        APIField("project_start_date"),
        APIField("project_end_date"),

    ]

    search_fields = ArticlePage.search_fields + [
        index.FilterField("project_start_date"),
        index.FilterField("project_end_date"),
    ]

class ArticleListingPage(MetadataPageMixin,
                            Page,
                            HeaderedPageMixin,
                            NavigationPageMixin):
    template = "website/pages/article_listing_page.html"

    def get_context(self,request):
        context = super().get_context(request)

        children = self.get_descendants().live().order_by('-first_published_at').specific()

        context['articles'] = children 

        return context

    class ArticlesSerializerField(Field):
        def to_representation(self,value):
            output = []
            
            for article in value:
                output += [{ 
                        "id":article.pk
                    }]
            return output

    @property
    def articles(self):
        return ArticlePage.objects.descendant_of(self).live().order_by('-first_published_at').specific().filter(show_in_listings=True)


    content_panels = Page.content_panels + HeaderedPageMixin.content_panels + NavigationPageMixin.content_panels + [
    ]

    api_fields = [
        APIField("articles",serializer=ArticlesSerializerField()),
    ]
