from django import forms
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.db import models
from django_json_widget.widgets import JSONEditorWidget
from django.contrib.auth.admin import UserAdmin
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.utils.safestring import mark_safe

# from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import  Service, Category_service


class Category_serviceAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('id', 'name')


class ServiceAdminForm(forms.ModelForm):
    extended_description = forms.CharField(widget=CKEditorUploadingWidget())
    # characteristics = forms.CharField(widget=CKEditorUploadingWidget())
    
    class Meta:
        model = Service
        fields = '__all__'


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    form = ServiceAdminForm
    formfield_overrides = {
        # fields.JSONField: {'widget': JSONEditorWidget}, # if django < 3.1
        models.JSONField: {'widget': JSONEditorWidget},
    }

    fields = ['name', 'photo', 'preview', 'short_description', 'price', 'cat', 'num_top', 'is_published', 'extended_description']
    list_display = ('id', 'name', 'price', 'author', 'time_create', 'author_last_update', 'time_update','num_top', 'is_published')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'price', 'short_description', 'author', 'time_create', 'author_last_update', 'time_update','num_top', 'is_published')
    list_editable = ('is_published', 'price', 'num_top',)
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

        super(ServiceAdmin, self).save_model(
            request=request,
            obj=obj,
            form=form,
            change=change
        )

admin.site.register(Category_service, Category_serviceAdmin)
