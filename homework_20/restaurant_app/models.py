from django.db import models
from django.urls import reverse

# Create your models here.
class Dish(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название блюда')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", default='defaults/default-images.jpg', verbose_name='Картинка')
    description = models.TextField(blank=True, verbose_name='Описание')
    price = models.PositiveIntegerField(verbose_name='Цена')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Категория')
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("dish", kwargs={"dish_slug": self.slug})
    
    def update_url(self):
        return reverse("update_dish", kwargs={"dish_slug": self.slug})
    
    def delete_url(self):
        return reverse("delete_dish", kwargs={"dish_slug": self.slug})
    
    class Meta:
        verbose_name = 'Блюдо'
        verbose_name_plural = 'Блюда'
        ordering = ['name']
    
    
    
class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название категории')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", default='defaults/default-image.jpg', verbose_name='Картинка')
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('category', kwargs={'category_slug': self.slug})
    
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['id']
        
        
        