# Generated by Django 5.0.5 on 2024-05-30 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0004_alter_livros_formato"),
    ]

    operations = [
        migrations.AlterField(
            model_name="livros",
            name="formato",
            field=models.CharField(
                choices=[("Ebook", "Ebook"), ("Fisico", "Fisico")], max_length=20
            ),
        ),
    ]
