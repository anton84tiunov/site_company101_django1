from django import forms
from django_json_widget.widgets import JSONEditorWidget                                                            
from .models import Service


class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        exclude = ["author", "author_last_update"]
        fields = ('extended_descript',)

