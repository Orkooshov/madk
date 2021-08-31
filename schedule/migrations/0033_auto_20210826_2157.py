# Generated by Django 3.2.6 on 2021-08-26 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0032_auto_20210826_0736'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='schedule',
            name='status',
        ),
        migrations.AddField(
            model_name='schedule',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Активен?'),
        ),
    ]
