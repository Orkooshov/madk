# Generated by Django 3.2.4 on 2021-08-14 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0018_alter_schedule_subgroup'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='status',
            field=models.IntegerField(choices=[(0, 'Учеба'), (1, 'Практика'), (2, 'Экзамены')], default=0),
        ),
    ]
