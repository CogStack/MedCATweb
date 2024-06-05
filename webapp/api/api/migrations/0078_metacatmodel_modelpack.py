# Generated by Django 2.2.28 on 2024-06-05 23:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0077_projectgroup_create_associated_projects'),
    ]

    operations = [
        migrations.CreateModel(
            name='MetaCATModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('meta_cat_dir', models.FilePathField(allow_folders=True, help_text='The zip or dir for a MetaCAT model')),
                ('meta_task', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.MetaTask')),
            ],
        ),
        migrations.CreateModel(
            name='ModelPack',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('model_pack', models.FileField(help_text='Model pack zip', upload_to='')),
                ('concept_db', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.ConceptDB')),
                ('meta_cats', models.ManyToManyField(blank=True, default=None, to='api.MetaCATModel')),
                ('vocab', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Vocabulary')),
            ],
        ),
    ]
