# Generated by Django 2.1.5 on 2020-01-30 12:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
        ('analytics', '0003_auto_20200130_1252'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='view',
            name='post',
        ),
        migrations.AddField(
            model_name='view',
            name='post',
            field=models.OneToOneField(blank=True, default=True, on_delete=django.db.models.deletion.CASCADE, related_name='view', to='posts.Post'),
        ),
    ]
