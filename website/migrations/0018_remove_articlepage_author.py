# Generated by Django 3.0.8 on 2020-07-22 16:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0017_articlepage_short_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articlepage',
            name='author',
        ),
    ]
