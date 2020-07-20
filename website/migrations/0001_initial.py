# Generated by Django 3.0.8 on 2020-07-20 15:57

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.blocks
import wagtail.core.fields
import wagtailmetadata.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailimages', '0022_uploadedimage'),
        ('wagtailcore', '0045_assign_unlock_grouppagepermission'),
    ]

    operations = [
        migrations.CreateModel(
            name='Footer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('social_items', wagtail.core.fields.StreamField([('social_link', wagtail.core.blocks.StructBlock([('link', wagtail.core.blocks.URLBlock()), ('social_type', wagtail.core.blocks.ChoiceBlock(choices=[('fb', 'facebook'), ('tt', 'twitter'), ('li', 'linked-in'), ('gh', 'github')]))]))])),
            ],
        ),
        migrations.CreateModel(
            name='Header',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('heading', models.CharField(max_length=255)),
                ('lead_paragraph', models.CharField(max_length=255)),
                ('fill_view_height', models.BooleanField(default=False)),
                ('background_image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
            ],
        ),
        migrations.CreateModel(
            name='Navbar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('menu_items', wagtail.core.fields.StreamField([('external_link', wagtail.core.blocks.StructBlock([('display_text', wagtail.core.blocks.CharBlock(required=False)), ('fa_icon_class', wagtail.core.blocks.CharBlock(required=False)), ('link', wagtail.core.blocks.URLBlock()), ('children', wagtail.core.blocks.StreamBlock([('external_link', wagtail.core.blocks.StructBlock([('display_text', wagtail.core.blocks.CharBlock(required=False)), ('fa_icon_class', wagtail.core.blocks.CharBlock(required=False)), ('link', wagtail.core.blocks.URLBlock())])), ('page_link', wagtail.core.blocks.StructBlock([('display_text', wagtail.core.blocks.CharBlock(required=False)), ('fa_icon_class', wagtail.core.blocks.CharBlock(required=False)), ('page', wagtail.core.blocks.PageChooserBlock())]))], required=False))])), ('page_link', wagtail.core.blocks.StructBlock([('display_text', wagtail.core.blocks.CharBlock(required=False)), ('fa_icon_class', wagtail.core.blocks.CharBlock(required=False)), ('page', wagtail.core.blocks.PageChooserBlock()), ('children', wagtail.core.blocks.StreamBlock([('external_link', wagtail.core.blocks.StructBlock([('display_text', wagtail.core.blocks.CharBlock(required=False)), ('fa_icon_class', wagtail.core.blocks.CharBlock(required=False)), ('link', wagtail.core.blocks.URLBlock())])), ('page_link', wagtail.core.blocks.StructBlock([('display_text', wagtail.core.blocks.CharBlock(required=False)), ('fa_icon_class', wagtail.core.blocks.CharBlock(required=False)), ('page', wagtail.core.blocks.PageChooserBlock())]))], required=False))]))])),
            ],
        ),
        migrations.CreateModel(
            name='StoryHomePage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('footer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='website.Footer')),
                ('header', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='website.Header')),
                ('navbar', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='website.Navbar')),
                ('search_image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image', verbose_name='Search image')),
            ],
            options={
                'abstract': False,
            },
            bases=(wagtailmetadata.models.MetadataMixin, 'wagtailcore.page', models.Model),
        ),
    ]
