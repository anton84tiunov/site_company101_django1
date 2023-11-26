from django import forms
from django_json_widget.widgets import JSONEditorWidget                                                            
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ["author", "author_last_update"]
        fields = ('extended_description',)

