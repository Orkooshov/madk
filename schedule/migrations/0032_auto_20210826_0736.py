# Generated by Django 3.2.6 on 2021-08-26 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0031_auto_20210821_1426'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='schedule',
            options={'ordering': ['group', 'weekday', 'lesson', 'week', 'subgroup'], 'verbose_name': 'Расписание', 'verbose_name_plural': 'Расписания'},
        ),
        migrations.RenameField(
            model_name='schedule',
            old_name='position',
            new_name='lesson',
        ),
        migrations.AlterField(
            model_name='schedule',
            name='weekday',
            field=models.IntegerField(choices=[(0, 'Понедельник'), (1, 'Вторник'), (2, 'Среда'), (3, 'Четверг'), (4, 'Пятница'), (5, 'Суббота'), (6, 'Воскресенье')], verbose_name='День недели'),
        ),
    ]
