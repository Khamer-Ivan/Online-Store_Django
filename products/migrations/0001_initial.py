# Generated by Django 4.1.7 on 2023-06-25 09:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('my_store_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(max_length=50, verbose_name='название категории')),
                ('image', models.FileField(null=True, upload_to='my_store_app/static/')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField(default=0, verbose_name='цена товара')),
                ('count', models.IntegerField(default=0, verbose_name='количество ')),
                ('date', models.DateField(auto_now_add=True)),
                ('title', models.TextField(max_length=50, verbose_name='название товара')),
                ('description', models.TextField(max_length=100, verbose_name='описание товара')),
                ('free_delivery', models.BooleanField(default=True)),
                ('product_picture', models.ImageField(null=True, upload_to='my_store_app/static/')),
                ('rating', models.IntegerField(default=0, verbose_name='счетчик покупок данного товара')),
                ('reviews', models.IntegerField(default=0, verbose_name='счетчик просмотров данного товара')),
                ('limited_edition', models.BooleanField(default=False, null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category', to='products.categoryproduct', verbose_name='категория товара')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
            },
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shop_name', models.TextField(max_length=50, verbose_name='название магазина')),
            ],
            options={
                'verbose_name': 'магазин',
                'verbose_name_plural': 'магазины',
            },
        ),
        migrations.CreateModel(
            name='Specifications',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=50, verbose_name='название')),
                ('value', models.TextField(max_length=50, verbose_name='значение')),
            ],
            options={
                'verbose_name': 'Спецификация',
                'verbose_name_plural': 'Спецификации',
            },
        ),
        migrations.CreateModel(
            name='TagsFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tags_name', models.TextField(max_length=50, verbose_name='тэг товара')),
            ],
            options={
                'verbose_name': 'Тэг',
                'verbose_name_plural': 'Тэги',
            },
        ),
        migrations.CreateModel(
            name='Sales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(default=0, verbose_name='количество товара по скидке')),
                ('dateFrom', models.DateField()),
                ('dateTo', models.DateField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product', verbose_name='товар')),
                ('shop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.shop', verbose_name='магазин')),
            ],
            options={
                'verbose_name': 'Распродажа',
                'verbose_name_plural': 'Распродажа',
            },
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(blank=True, default='Не указано', max_length=100, verbose_name='текст отзыва')),
                ('create_at', models.DateField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_store_app.profile', verbose_name='пользователь')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_title_product_set', to='products.product', verbose_name='товар')),
            ],
            options={
                'verbose_name': 'Отзыв',
                'verbose_name_plural': 'Отзывы',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='shop',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shop', to='products.shop', verbose_name='магазин товара'),
        ),
        migrations.AddField(
            model_name='product',
            name='specifications',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.specifications', verbose_name='спецификация товара'),
        ),
        migrations.AddField(
            model_name='product',
            name='tags',
            field=models.ManyToManyField(related_name='tags', to='products.tagsfile'),
        ),
    ]