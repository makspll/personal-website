# Generated by Django 3.1 on 2020-08-23 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0045_auto_20200811_2225'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectarticlepage',
            name='is_coursework',
            field=models.BooleanField(default=False),
        ),
    ]
