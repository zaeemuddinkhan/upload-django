# Generated by Django 4.1.6 on 2023-07-25 17:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('du2', '0005_rename_posts_comment_post'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='post',
            new_name='posts',
        ),
    ]
