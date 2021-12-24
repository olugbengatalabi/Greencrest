# Generated by Django 3.2.6 on 2021-12-23 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_auto_20211224_0014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('CT', 'Cactus'), ('FL', 'Flowering'), ('S', 'Succulent'), ('F', 'Fern'), ('CL', 'Climbing')], max_length=2),
        ),
        migrations.AlterField(
            model_name='product',
            name='label',
            field=models.CharField(blank=True, choices=[('D', 'danger'), ('P', 'primary'), ('S', 'secondary')], max_length=1, null=True),
        ),
    ]