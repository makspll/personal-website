# Generated by Django 3.0.8 on 2020-07-22 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0016_articlepage_projectarticlepage'),
    ]

    operations = [
        migrations.AddField(
            model_name='articlepage',
            name='short_title',
            field=models.CharField(default='Article', max_length=255),
        ),
    ]