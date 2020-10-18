# Generated by Django 2.2.10 on 2020-09-09 11:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20200909_0914'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeacherProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(default='', max_length=60, null=True)),
                ('phone', models.CharField(default='', max_length=60, null=True)),
                ('address', models.CharField(default='', max_length=255, null=True)),
                ('date_of_birth', models.CharField(default='', max_length=60, null=True)),
                ('blood_group', models.CharField(default='', max_length=60, null=True)),
                ('gender', models.CharField(default='', max_length=60, null=True)),
                ('religion', models.CharField(default='', max_length=60, null=True)),
                ('initial', models.CharField(default='', max_length=60, null=True)),
                ('image', models.ImageField(default='', null=True, upload_to='images/%Y/%m/%d/')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='StudentProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=60, null=True)),
                ('phone', models.CharField(max_length=60, null=True)),
                ('address', models.CharField(max_length=255, null=True)),
                ('date_of_birth', models.CharField(max_length=60, null=True)),
                ('blood_group', models.CharField(max_length=60, null=True)),
                ('gender', models.CharField(max_length=60, null=True)),
                ('department', models.CharField(max_length=60, null=True)),
                ('religion', models.CharField(max_length=60, null=True)),
                ('image', models.FileField(null=True, upload_to='images/%Y/%m/%d/')),
                ('update_on', models.DateTimeField(auto_now_add=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]