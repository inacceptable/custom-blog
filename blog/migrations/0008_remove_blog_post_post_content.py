# Generated by Django 2.0.13 on 2021-09-26 07:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20210926_1650'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog_post',
            name='post_content',
        ),
    ]