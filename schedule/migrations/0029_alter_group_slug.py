# Generated by Django 3.2.4 on 2021-08-21 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0028_auto_20210821_1406'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]
