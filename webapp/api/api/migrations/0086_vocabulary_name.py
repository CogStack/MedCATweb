# Generated by Django 5.1.4 on 2025-01-30 00:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0085_alter_conceptdb_name_alter_dataset_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='vocabulary',
            name='name',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
    ]
