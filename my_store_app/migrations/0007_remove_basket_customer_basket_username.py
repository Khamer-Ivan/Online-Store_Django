# Generated by Django 4.1.7 on 2023-04-24 11:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('my_store_app', '0006_rename_username_basket_customer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='basket',
            name='customer',
        ),
        migrations.AddField(
            model_name='basket',
            name='username',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, null=True, related_name='profile', to='my_store_app.profile'),
        ),
    ]
