# Generated by Django 4.2.4 on 2023-08-18 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='photo',
            field=models.ImageField(default='defaults/default-images.jpg', upload_to='photos/%Y/%m/%d/', verbose_name='Картинка'),
        ),
        migrations.AddField(
            model_name='dish',
            name='photo',
            field=models.ImageField(default='defaults/default-images.jpg', upload_to='photos/%Y/%m/%d/', verbose_name='Картинка'),
        ),
    ]