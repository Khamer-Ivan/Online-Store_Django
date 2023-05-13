# Generated by Django 4.1.7 on 2023-05-13 12:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('my_store_app', '0010_cart_delete_basket'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='product_order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_order', to='my_store_app.product', verbose_name='товар'),
        ),
    ]
