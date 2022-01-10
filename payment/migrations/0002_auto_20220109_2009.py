# Generated by Django 3.2.6 on 2022-01-09 19:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0003_alter_cartitem_line_total'),
        ('payment', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='one_click_purchasing',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='stripe_customer_id',
        ),
        migrations.AddField(
            model_name='payment',
            name='cart',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='cart.cart'),
            preserve_default=False,
        ),
    ]