# Generated by Django 3.1.6 on 2021-03-08 22:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20210308_1710'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='post_caption',
            new_name='caption',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='post_date',
            new_name='date',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='post_image',
            new_name='image',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='post_user',
            new_name='user',
        ),
    ]