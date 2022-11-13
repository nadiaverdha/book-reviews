# Generated by Django 4.1.3 on 2022-11-13 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("book", "0011_alter_bookinstance_status_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="bookinstance",
            name="status",
            field=models.CharField(
                blank=True,
                choices=[
                    ("w", "want to read"),
                    ("r", "read"),
                    ("cr", "currently reading"),
                ],
                default="w",
                help_text="Book status",
                max_length=2,
            ),
        ),
    ]
