# Generated by Django 5.1.4 on 2025-01-29 23:30

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0084_conceptdb_create_time_conceptdb_last_modified_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conceptdb',
            name='name',
            field=models.CharField(blank=True, default='', max_length=100, unique=True, validators=[django.core.validators.RegexValidator('^[0-9a-zA-Z_-]*$', 'Only alpahanumeric characters, -, _ are allowed for CDB names')]),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='name',
            field=models.CharField(max_length=150, unique=True),
        ),
        migrations.AlterField(
            model_name='metacatmodel',
            name='name',
            field=models.CharField(help_text='The task name followed by the underlying model impl', max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='metataskvalue',
            name='name',
            field=models.CharField(max_length=150, unique=True),
        ),
        migrations.AlterField(
            model_name='modelpack',
            name='name',
            field=models.TextField(unique=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='name',
            field=models.CharField(help_text='A name of the annotation project', max_length=150, unique=True),
        ),
        migrations.AlterField(
            model_name='projectgroup',
            name='name',
            field=models.CharField(help_text='A name of the annotation project', max_length=150, unique=True),
        ),
    ]
