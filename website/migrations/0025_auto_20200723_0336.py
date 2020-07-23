# Generated by Django 3.0.8 on 2020-07-23 03:36

from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
        ('website', '0024_articlelistingpage_lead_paragraph'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content_object', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.ArticlePage')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='website_articletag_items', to='taggit.Tag')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='articlepage',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='website.ArticleTag', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]
