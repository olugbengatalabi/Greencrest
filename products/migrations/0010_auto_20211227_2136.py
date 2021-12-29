# Generated by Django 3.2.6 on 2021-12-27 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_auto_20211224_0033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('CL', 'Climbing'), ('FL', 'Flowering'), ('CT', 'Cactus'), ('S', 'Succulent'), ('F', 'Fern')], max_length=2),
        ),
        migrations.AlterField(
            model_name='product',
            name='label',
            field=models.CharField(blank=True, choices=[('P', 'primary'), ('S', 'secondary'), ('D', 'danger')], max_length=1, null=True),
        ),
    ]
