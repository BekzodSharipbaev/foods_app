from django.contrib import admin

from .models import *

# Register your models here.
class DishAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'photo', 'description', 'price', 'category',)
    list_display_links = ('name', 'category',)
    list_filter = ('price',)
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}
    
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'photo', )
    list_display_links = ('name',)
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}
    

admin.site.register(Dish, DishAdmin)
admin.site.register(Category, CategoryAdmin)
