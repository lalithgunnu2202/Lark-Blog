# Generated by Django 5.2.3 on 2025-06-11 10:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_blog_data_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog_data',
            old_name='blog',
            new_name='disc',
        ),
    ]
