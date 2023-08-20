from django import forms

from .models import *


class AddDishForm(forms.ModelForm):
    class Meta:
        model = Dish
        fields = ['name', 'slug', 'description', 'photo', 'price', 'category']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-input'}),
            'slug': forms.TextInput(attrs={'class': 'form-input'}),
            'description': forms.Textarea(attrs={'cols': 60, 'rows': 10}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].empty_label = 'Категория не выбрана'
        
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
    
    
    