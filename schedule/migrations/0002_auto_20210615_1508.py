# Generated by Django 3.2.4 on 2021-06-15 12:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='TeacherClassroom',
            new_name='Teacher_Classroom',
        ),
        migrations.RenameModel(
            old_name='TeacherSubject',
            new_name='Teacher_Subject',
        ),
    ]
