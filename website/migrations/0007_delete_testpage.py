# Generated by Django 3.0.8 on 2020-07-20 13:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailforms', '0004_add_verbose_name_plural'),
        ('wagtailcore', '0045_assign_unlock_grouppagepermission'),
        ('wagtailredirects', '0006_redirect_increase_max_length'),
        ('website', '0006_auto_20200718_1558'),
    ]

    operations = [
        migrations.DeleteModel(
            name='testPage',
        ),
    ]
