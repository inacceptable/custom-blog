# Generated by Django 2.0.13 on 2021-09-21 11:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20210918_2341'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog_change',
            old_name='navigation_bar_backgrond_color',
            new_name='navigation_bar_background_color',
        ),
    ]