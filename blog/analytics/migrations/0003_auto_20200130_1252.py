# Generated by Django 2.1.5 on 2020-01-30 12:52

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('analytics', '0002_auto_20200130_1247'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='view',
            name='post',
        ),
        migrations.AddField(
            model_name='view',
            name='post',
            field=models.ManyToManyField(related_name='view', to='posts.Post'),
        ),
        migrations.RemoveField(
            model_name='view',
            name='user',
        ),
        migrations.AddField(
            model_name='view',
            name='user',
            field=models.ManyToManyField(related_name='views', to=settings.AUTH_USER_MODEL),
        ),
    ]
