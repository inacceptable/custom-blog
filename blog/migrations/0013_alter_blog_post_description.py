# Generated by Django 3.2.8 on 2021-11-04 02:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_alter_blog_post_post_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog_post',
            name='description',
            field=models.TextField(default='Test'),
            preserve_default=False,
        ),
    ]
