# Generated by Django 4.2.3 on 2023-09-26 23:52

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("news", "0008_alter_news_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="news",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to="img/"),
        ),
    ]
