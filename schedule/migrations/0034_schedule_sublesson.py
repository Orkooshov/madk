# Generated by Django 3.2.6 on 2021-08-26 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0033_auto_20210826_2157'),
    ]

    operations = [
        migrations.AddField(
            model_name='schedule',
            name='sublesson',
            field=models.IntegerField(choices=[(0, 'Вся пара'), (1, 'Первая половина'), (2, 'Вторая половина')], default=0, verbose_name='Длительность'),
        ),
    ]
