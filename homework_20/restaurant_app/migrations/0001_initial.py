# Generated by Django 4.2.4 on 2023-08-17 19:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название категории')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Dish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название блюда')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
                ('price', models.PositiveIntegerField(verbose_name='Цена')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='restaurant_app.category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Блюдо',
                'verbose_name_plural': 'Блюда',
                'ordering': ['name'],
            },
        ),
    ]
