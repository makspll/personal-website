# Generated by Django 3.0.8 on 2020-07-22 22:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0021_auto_20200722_2209'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectarticlepage',
            name='project_end_date',
            field=models.DateField(blank=True, default=datetime.date.today, null=True),
        ),
        migrations.AddField(
            model_name='projectarticlepage',
            name='project_start_date',
            field=models.DateField(blank=True, default=datetime.date.today, null=True),
        ),
    ]
