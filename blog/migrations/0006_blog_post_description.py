# Generated by Django 2.0.13 on 2021-09-26 06:37

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20210921_2145'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog_post',
            name='description',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]