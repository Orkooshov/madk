# Generated by Django 3.2.4 on 2021-08-21 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0029_alter_group_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='slug',
            field=models.SlugField(unique=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]