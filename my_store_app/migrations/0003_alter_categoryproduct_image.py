# Generated by Django 4.1.7 on 2023-03-27 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_store_app', '0002_alter_categoryproduct_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoryproduct',
            name='image',
            field=models.FileField(null=True, upload_to='my_store_app/static/'),
        ),
    ]