# Generated by Django 3.2.8 on 2021-12-06 01:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0018_blog_change_section_border_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog_post',
            name='topic',
            field=models.ForeignKey(null='True', on_delete=django.db.models.deletion.CASCADE, to='blog.topic'),
        ),
    ]
