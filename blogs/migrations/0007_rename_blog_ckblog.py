# Generated by Django 5.0.2 on 2025-01-29 16:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0006_blog_alter_blogs_blog_body'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Blog',
            new_name='CKBlog',
        ),
    ]
