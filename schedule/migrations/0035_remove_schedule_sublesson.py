# Generated by Django 3.2.6 on 2021-08-26 20:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0034_schedule_sublesson'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='schedule',
            name='sublesson',
        ),
    ]
