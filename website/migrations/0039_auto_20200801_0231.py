# Generated by Django 3.0.8 on 2020-08-01 01:31

from django.db import migrations, models
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0038_auto_20200731_2346'),
    ]

    operations = [
        migrations.AddField(
            model_name='articlepage',
            name='tag_line',
            field=models.CharField(default='Describe your article in a few words', max_length=255),
        ),
        migrations.AlterField(
            model_name='articlepage',
            name='blurb',
            field=wagtail.core.fields.RichTextField(default='introduce your article'),
        ),
    ]
