# Generated by Django 3.2.6 on 2021-12-27 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitem',
            name='line_total',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=100, null=True),
        ),
    ]
