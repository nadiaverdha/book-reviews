# Generated by Django 4.1.2 on 2022-11-19 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("book", "0032_alter_bookinstance_status"),
    ]

    operations = [
        migrations.AlterField(
            model_name="bookinstance",
            name="status",
            field=models.CharField(
                blank=True,
                choices=[
                    ("cr", "currently reading"),
                    ("w", "want to read"),
                    ("r", "read"),
                ],
                default="w",
                help_text="Book status",
                max_length=2,
            ),
        ),
        migrations.AddConstraint(
            model_name="bookinstance",
            constraint=models.UniqueConstraint(
                fields=("book", "user"), name="uq_bookinstance_book_user"
            ),
        ),
    ]