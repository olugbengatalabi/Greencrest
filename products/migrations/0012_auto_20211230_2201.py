# Generated by Django 3.2.6 on 2021-12-30 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_alter_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('F', 'Fern'), ('CL', 'Climbing'), ('CT', 'Cactus'), ('FL', 'Flowering'), ('S', 'Succulent')], max_length=2),
        ),
        migrations.AlterField(
            model_name='product',
            name='label',
            field=models.CharField(blank=True, choices=[('D', 'danger'), ('P', 'primary'), ('S', 'secondary')], max_length=1, null=True),
        ),
    ]
