# Generated by Django 5.0.7 on 2024-07-13 00:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_blogtagindexpage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpage',
            name='tags',
        ),
        migrations.RemoveField(
            model_name='blogtagindexpage',
            name='page_ptr',
        ),
        migrations.DeleteModel(
            name='BlogPageTag',
        ),
        migrations.DeleteModel(
            name='BlogTagIndexPage',
        ),
    ]
