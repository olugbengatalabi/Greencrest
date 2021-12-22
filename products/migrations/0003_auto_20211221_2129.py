# Generated by Django 3.2.6 on 2021-12-21 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20211221_2127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('FL', 'Flowering'), ('CT', 'Cactus'), ('F', 'Fern'), ('CL', 'Climbing'), ('S', 'Succulent')], max_length=2),
        ),
        migrations.AlterField(
            model_name='product',
            name='label',
            field=models.CharField(blank=True, choices=[('D', 'danger'), ('P', 'primary'), ('S', 'secondary')], max_length=1, null=True),
        ),
    ]
