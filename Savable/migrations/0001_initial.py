# Generated by Django 5.0.6 on 2024-05-13 17:00

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ThreeVennDiagram',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field1', models.TextField()),
                ('field2', models.TextField()),
                ('field3', models.TextField()),
                ('filter', models.TextField(null=True)),
                ('user_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ThreeProblemStatement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('statement', models.TextField()),
                ('user_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('venn_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Savable.threevenndiagram')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TwoVennDiagram',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field1', models.TextField()),
                ('field2', models.TextField()),
                ('field3', models.TextField()),
                ('filter', models.TextField(null=True)),
                ('user_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TwoProblemStatement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('statement', models.TextField()),
                ('user_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('venn_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Savable.twovenndiagram')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]