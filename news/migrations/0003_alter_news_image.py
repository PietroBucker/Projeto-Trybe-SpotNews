# Generated by Django 4.2.3 on 2023-09-26 00:32

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("news", "0002_alter_news_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="news",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to="img"),
        ),
    ]
