from django import forms
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.db import models
from django_json_widget.widgets import JSONEditorWidget
from django.contrib.auth.admin import UserAdmin
from django.utils.safestring import mark_safe

from ckeditor_uploader.widgets import CKEditorUploadingWidget

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser, News, Category_news



class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username',]


class Category_newsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('id', 'name')

class NewsAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())
    # text1 = forms.CharField(widget=CKEditorUploadingWidget())
    # text2 = forms.CharField(widget=CKEditorUploadingWidget())
    # text3 = forms.CharField(widget=CKEditorUploadingWidget())
    # text4 = forms.CharField(widget=CKEditorUploadingWidget())
    # text5 = forms.CharField(widget=CKEditorUploadingWidget())
    # text6 = forms.CharField(widget=CKEditorUploadingWidget())
    
    class Meta:
        model = News
        fields = '__all__'


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    form = NewsAdminForm
    formfield_overrides = {
        # fields.JSONField: {'widget': JSONEditorWidget}, # if django < 3.1
        models.JSONField: {'widget': JSONEditorWidget},
    }

    fields = ['title', 'photo', 'preview', 'short_description', 'cat', 'content', 'num_top', 'is_published', 'contents', 'contents_style', 'contents_script']
    list_display = ('id', 'title','preview' , 'author', 'time_create', 'author_last_update', 'time_update','num_top', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content', 'author', 'time_create', 'author_last_update', 'time_update','num_top', 'is_published')
    list_editable = ('is_published', 'num_top',)
    readonly_fields = ["preview"]
    
    def preview(self, obj):
        return mark_safe(f'<img src="{obj.photo.url}" style="max-height: 50px;">')


    #  # Вывод картинок в админке!
    # def image_img(self):
    #     if self.images:
    #         from django.utils.safestring import mark_safe
    #         return mark_safe(u'<a href="{0}" target="_blank"><img src="{0}" width="100"/></a>'.format(self.photo.url))
    #     else:
    #         return '(Нет изображения)'
    # image_img.short_description = 'Картинка'
    # image_img.allow_tags = True
    
    def save_model(self, request, obj, form, change):
        """
        Переопределяем метод сохранения модели
        """
        if not change: # Проверяем что запись только создаётся
            obj.author = request.user # Присваеваем полю автор текущего пользователя
        else:
            obj.author_last_update = request.user

        super(NewsAdmin, self).save_model(
            request=request,
            obj=obj,
            form=form,
            change=change
        )
admin.site.register(CustomUser, CustomUserAdmin)
# admin.site.register(News, NewsAdmin)
admin.site.register(Category_news, Category_newsAdmin)