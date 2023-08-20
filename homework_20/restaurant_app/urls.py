from django.urls import path

from .views import *

urlpatterns = [
    path('', DishesView.as_view(), name='dishes'),
    path('dish/<slug:dish_slug>/', DishView.as_view(), name='dish'),
    path('add_dish/', AddDishView.as_view(), name='add_dish'),
    path('dish/<slug:dish_slug>/update_dish/', UpdateDishView.as_view(), name='update_dish'),
    path('dish/<slug:dish_slug>/delete_dish/', DeleteDishView.as_view(), name='delete_dish'),
]
