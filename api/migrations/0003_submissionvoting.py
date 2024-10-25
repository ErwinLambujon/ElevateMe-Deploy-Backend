# Generated by Django 5.0.6 on 2024-10-25 03:00

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_submissioncomment'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubmissionVoting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marks', models.IntegerField(validators=[django.core.validators.MinValueValidator(1, message='Value must be at least 1'), django.core.validators.MaxValueValidator(10, message='Value cannot be greater than 10')])),
                ('member_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('submission_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.channelsubmission')),
            ],
        ),
    ]
