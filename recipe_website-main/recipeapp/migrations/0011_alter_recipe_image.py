# Generated by Django 4.2.6 on 2023-10-16 06:21

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("recipeapp", "0010_alter_recipe_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="recipe",
            name="image",
            field=models.ImageField(blank=True, upload_to="images/"),
        ),
    ]