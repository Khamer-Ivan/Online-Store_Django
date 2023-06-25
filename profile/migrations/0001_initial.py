# Generated by Django 4.1.7 on 2023-06-25 09:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import profile.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, default='-------', max_length=50, null=True, verbose_name='username')),
                ('full_name', models.CharField(blank=True, default='не указано', max_length=50, verbose_name='ФИО пользователя')),
                ('phone', models.CharField(blank=True, default='Не указано', max_length=30, null=True, unique=True, verbose_name='номер телефона')),
                ('email', models.EmailField(blank=True, max_length=254, unique=True, verbose_name='email пользователя')),
                ('avatar', models.ImageField(default='', null=True, upload_to='catalog/files/', validators=[profile.models.Profile.validate_image])),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Профиль',
                'verbose_name_plural': 'Профили пользователей',
            },
        ),
    ]