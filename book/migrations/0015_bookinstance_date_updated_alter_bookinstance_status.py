# Generated by Django 4.1.3 on 2022-11-13 18:20

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("book", "0014_alter_bookinstance_status"),
    ]

    operations = [
        migrations.AddField(
            model_name="bookinstance",
            name="date_updated",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="bookinstance",
            name="status",
            field=models.CharField(
                blank=True,
                choices=[
                    ("cr", "currently reading"),
                    ("r", "read"),
                    ("w", "want to read"),
                ],
                default="w",
                help_text="Book status",
                max_length=2,
            ),
        ),
    ]
