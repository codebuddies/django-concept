# Generated by Django 2.2.4 on 2020-03-03 20:57

from django.db import migrations, models
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0005_auto_20200118_1036'),
        ('tagging', '0001_initial')
    ]

    operations = [
        migrations.AlterField(
            model_name='resource',
            name='other_referring_source',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='resource',
            name='tags',
            field=taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='tagging.TaggedItems', to='tagging.CustomTag', verbose_name='Tags'),
        ),
    ]
