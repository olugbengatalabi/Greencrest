# Generated by Django 3.2.6 on 2021-12-23 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_auto_20211223_1938'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('FL', 'Flowering'), ('F', 'Fern'), ('CL', 'Climbing'), ('CT', 'Cactus'), ('S', 'Succulent')], max_length=2),
        ),
        migrations.AlterField(
            model_name='product',
            name='label',
            field=models.CharField(blank=True, choices=[('S', 'secondary'), ('P', 'primary'), ('D', 'danger')], max_length=1, null=True),
        ),
    ]
