# Generated by Django 4.2 on 2024-10-26 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_merge_20241026_0035'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='channelsubmission',
            name='submitted_work',
        ),
        migrations.AddField(
            model_name='channelsubmission',
            name='submitted_work_content',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='channelsubmission',
            name='submitted_work_name',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='channelsubmission',
            name='submitted_work_type',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
