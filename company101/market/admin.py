from django import forms
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.db import models
from django_json_widget.widgets import JSONEditorWidget
from django.contrib.auth.admin import UserAdmin
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.utils.safestring import mark_safe

# from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import  Product, Category_product


class Category_productAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('id', 'name')


class ProductAdminForm(forms.ModelForm):
    extended_description = forms.CharField(widget=CKEditorUploadingWidget())
    characteristics = forms.CharField(widget=CKEditorUploadingWidget())
    
    class Meta:
        model = Product
        fields = '__all__'


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    form = ProductAdminForm
    formfield_overrides = {
        # fields.JSONField: {'widget': JSONEditorWidget}, # if django < 3.1
        models.JSONField: {'widget': JSONEditorWidget},
    }

    fields = ['manufacturer', 'model', 'photo', 'preview', 'short_description', 'price', 'cat', 'num_top', 'is_published', 'is_availability', 'extended_description', 'characteristics']
    list_display = ('id', 'manufacturer', 'model', 'price', 'author', 'time_create', 'author_last_update', 'time_update','num_top', 'is_published', 'is_availability')
    list_display_links = ('id', 'manufacturer', 'model')
    search_fields = ('manufacturer','model', 'price', 'content', 'author', 'time_create', 'author_last_update', 'time_update','num_top', 'is_published', 'is_availability')
    list_editable = ('is_published', 'is_availability', 'price', 'num_top',)
    readonly_fields = ["preview"]


    def preview(self, obj):
        return mark_safe(f'<img src="{obj.photo.url}" style="max-height: 50px;">')
    
    def save_model(self, request, obj, form, change):
        """
        Переопределяем метод сохранения модели
        """
        if not change: # Проверяем что запись только создаётся
            obj.author = request.user # Присваеваем полю автор текущего пользователя
        else:
            obj.author_last_update = request.user

        super(ProductAdmin, self).save_model(
            request=request,
            obj=obj,
            form=form,
            change=change
        )

admin.site.register(Category_product, Category_productAdmin)
