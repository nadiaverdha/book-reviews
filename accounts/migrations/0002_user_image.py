# Generated by Django 4.1.3 on 2022-11-13 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="image",
            field=models.ImageField(default="no photo", upload_to=""),
        ),
    ]
