# Generated by Django 4.0.3 on 2022-03-31 18:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_rename_id_feed_feed_rename_id_story_story'),
    ]

    operations = [
        migrations.RenameField(
            model_name='feed',
            old_name='Feed',
            new_name='post',
        ),
        migrations.RenameField(
            model_name='story',
            old_name='Story',
            new_name='post',
        ),
    ]
