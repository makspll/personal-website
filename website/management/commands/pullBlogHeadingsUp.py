from django.core.management.base import BaseCommand, CommandError
from website.models import ArticlePage
import json
import re
from django.db import transaction

class Command(BaseCommand):
    help = 'pulls up headings in article pages and project article pages so that the biggest headings are h2'

    def handle_items(self,article,no_input=False):
        """
            given article_mixin extending article, pulls up headings in article_items stream field
        """
        
        handle_current = True
        if not no_input:
            handle_current = input('pull headings in article titled: {0}? [Y/n]:'.format(article.title)) == "Y" 
        
        if handle_current:
            with transaction.atomic():
                for article_item in article.article_items:
                    if article_item.block_type == "text":
                        rich_text = article_item.value.source
                        if "h2>" in article_item.value.source:
                            print("rich text block already contains h2 headers, skipping to avoid losing information.")
                        else: 
                            swapped_h3 = re.sub(r'h3\>','h2>', rich_text)
                            swapped_h4 = re.sub(r'h4\>','h3>', swapped_h3)
                            swapped_h5 = re.sub(r'h5\>','h5>', swapped_h4)
                            article_item.value.source = swapped_h5
                            print("pulled headings in rich text block.")
                
                article.save()
        else:
            pass

    def add_arguments(self,parser):
        parser.add_argument('--no-input',action="store_true",help="don't prompt at each change")
    def handle(self, *args, **options):

        all_articles = ArticlePage.objects.all()

        if len(all_articles) == 0:
            print("no articles present")
        else:
            no_input = 'no-input' in options

            # will do this for all articles inheriting from ArticlePage as well
            for article in all_articles:
                self.handle_items(article,no_input)
