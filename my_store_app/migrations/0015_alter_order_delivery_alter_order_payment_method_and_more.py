# Generated by Django 4.1.7 on 2023-06-05 20:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('my_store_app', '0014_alter_order_product_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='delivery',
            field=models.CharField(choices=[('reg', 'Обычная доставка'), ('exp', 'Экспресс доставка')], default='reg', max_length=3, verbose_name='delivery'),
        ),
        migrations.AlterField(
            model_name='order',
            name='payment_method',
            field=models.CharField(choices=[('card', 'Онлайн картой'), ('cash', 'Онлайн со случайного чужого счета')], default='card', max_length=4, verbose_name='payment method'),
        ),
        migrations.CreateModel(
            name='ProductInOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='order', to='my_store_app.order')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='prod', to='my_store_app.product')),
            ],
        ),
    ]