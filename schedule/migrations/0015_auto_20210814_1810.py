# Generated by Django 3.2.4 on 2021-08-14 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0014_auto_20210707_1528'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='schedulestatus',
            options={'ordering': ['pk'], 'verbose_name': 'Этап обучения', 'verbose_name_plural': 'Этапы обучения'},
        ),
        migrations.AlterField(
            model_name='weekday',
            name='name',
            field=models.CharField(max_length=16),
        ),
    ]