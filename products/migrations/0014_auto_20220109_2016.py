# Generated by Django 3.2.6 on 2022-01-09 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0013_auto_20220109_2009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('CT', 'Cactus'), ('CL', 'Climbing'), ('FL', 'Flowering'), ('S', 'Succulent'), ('F', 'Fern')], max_length=2),
        ),
        migrations.AlterField(
            model_name='product',
            name='label',
            field=models.CharField(blank=True, choices=[('P', 'primary'), ('D', 'danger'), ('S', 'secondary')], max_length=1, null=True),
        ),
    ]
