# Generated by Django 4.1.7 on 2023-03-26 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0002_alter_blog_writer"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blog", name="writer", field=models.TextField(max_length=100),
        ),
    ]
