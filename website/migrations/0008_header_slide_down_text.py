# Generated by Django 3.0.8 on 2020-07-21 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0007_auto_20200720_1910'),
    ]

    operations = [
        migrations.AddField(
            model_name='header',
            name='slide_down_text',
            field=models.CharField(default='Slide Down', max_length=255),
        ),
    ]