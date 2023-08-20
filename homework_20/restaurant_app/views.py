from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import *
from .forms import AddDishForm

# Create your views here.

class DishesView(ListView):
    model = Dish
    template_name = 'restaurant_app/dishes.html'
    context_object_name = 'dishes'
    

class DishView(DetailView):
    model = Dish
    template_name = 'restaurant_app/dish.html'
    context_object_name = 'dish'
    slug_url_kwarg = 'dish_slug'


class AddDishView(CreateView):
    form_class = AddDishForm
    template_name = 'restaurant_app/add_dish.html'
    success_url = reverse_lazy('dishes')


class UpdateDishView(UpdateView):
    model = Dish
    template_name = 'restaurant_app/update_dish.html'
    slug_url_kwarg = 'dish_slug'
    form_class = AddDishForm
    
    def get_success_url(self) -> str:
        return reverse_lazy("dish", args=(self.kwargs['dish_slug'],))
    
class DeleteDishView(DeleteView):
    model = Dish
    template_name = 'restaurant_app/delete_dish.html'
    slug_url_kwarg = 'dish_slug'
    success_url = reverse_lazy('dishes')
    
        
        
    