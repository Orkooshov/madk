# Generated by Django 3.2.4 on 2021-08-19 16:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0024_alter_schedule_weekday'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Weekday',
        ),
    ]
