# Generated by Django 4.0.2 on 2022-02-17 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_remove_blog_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='story',
            field=models.CharField(max_length=255),
        ),
    ]
