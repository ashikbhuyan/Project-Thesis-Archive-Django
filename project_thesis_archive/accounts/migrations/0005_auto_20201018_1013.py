# Generated by Django 2.2.10 on 2020-10-18 10:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_remove_studentprofile_full_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacherprofile',
            name='user',
        ),
        migrations.DeleteModel(
            name='StudentProfile',
        ),
        migrations.DeleteModel(
            name='TeacherProfile',
        ),
    ]
