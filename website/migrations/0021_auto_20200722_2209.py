# Generated by Django 3.0.8 on 2020-07-22 22:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0020_articlepage_content'),
    ]

    operations = [
        migrations.RenameField(
            model_name='articlepage',
            old_name='content',
            new_name='article_items',
        ),
    ]
