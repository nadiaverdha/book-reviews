# Generated by Django 4.1.3 on 2022-11-16 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("book", "0026_alter_bookinstance_status"),
    ]

    operations = [
        migrations.AlterField(
            model_name="bookinstance",
            name="status",
            field=models.CharField(
                blank=True,
                choices=[
                    ("r", "read"),
                    ("cr", "currently reading"),
                    ("w", "want to read"),
                ],
                default="w",
                help_text="Book status",
                max_length=2,
            ),
        ),
    ]
