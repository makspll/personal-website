# Generated by Django 3.0.8 on 2020-07-27 14:30

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0029_navbar_automatic_items_mode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='navbar',
            name='menu_items',
            field=wagtail.core.fields.StreamField([('external_link', wagtail.core.blocks.StructBlock([('display_text', wagtail.core.blocks.CharBlock(required=False)), ('fa_icon_class', wagtail.core.blocks.CharBlock(required=False)), ('link', wagtail.core.blocks.URLBlock()), ('children', wagtail.core.blocks.StreamBlock([('external_link', wagtail.core.blocks.StructBlock([('display_text', wagtail.core.blocks.CharBlock(required=False)), ('fa_icon_class', wagtail.core.blocks.CharBlock(required=False)), ('link', wagtail.core.blocks.URLBlock())])), ('page_link', wagtail.core.blocks.StructBlock([('display_text', wagtail.core.blocks.CharBlock(required=False)), ('fa_icon_class', wagtail.core.blocks.CharBlock(required=False)), ('page', wagtail.core.blocks.PageChooserBlock())]))], required=False))])), ('page_link', wagtail.core.blocks.StructBlock([('display_text', wagtail.core.blocks.CharBlock(required=False)), ('fa_icon_class', wagtail.core.blocks.CharBlock(required=False)), ('page', wagtail.core.blocks.PageChooserBlock()), ('children', wagtail.core.blocks.StreamBlock([('external_link', wagtail.core.blocks.StructBlock([('display_text', wagtail.core.blocks.CharBlock(required=False)), ('fa_icon_class', wagtail.core.blocks.CharBlock(required=False)), ('link', wagtail.core.blocks.URLBlock())])), ('page_link', wagtail.core.blocks.StructBlock([('display_text', wagtail.core.blocks.CharBlock(required=False)), ('fa_icon_class', wagtail.core.blocks.CharBlock(required=False)), ('page', wagtail.core.blocks.PageChooserBlock())]))], required=False))]))], blank=True, null=True),
        ),
    ]
