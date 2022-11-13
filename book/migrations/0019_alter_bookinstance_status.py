# Generated by Django 4.1.3 on 2022-11-13 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("book", "0018_bookinstance_date_updated"),
    ]

    operations = [
        migrations.AlterField(
            model_name="bookinstance",
            name="status",
            field=models.CharField(
                blank=True,
                choices=[
                    ("w", "want to read"),
                    ("cr", "currently reading"),
                    ("r", "read"),
                ],
                default="w",
                help_text="Book status",
                max_length=2,
            ),
        ),
    ]