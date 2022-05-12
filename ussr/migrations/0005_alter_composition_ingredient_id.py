# Generated by Django 4.0.4 on 2022-05-12 15:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ussr', '0004_remove_composition_ingredient_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='composition',
            name='ingredient_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ussr.ingredient', verbose_name='ингредиент'),
        ),
    ]
