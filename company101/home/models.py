import os
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
# from django.contrib.postgres.fields import ArrayField

class CustomUser(AbstractUser):
    is_news_update = models.BooleanField(default=False)
    is_news_insert = models.BooleanField(default=False)
    is_news_delete = models.BooleanField(default=False)

    # add additional fields in here
# RENAME TABLE home_category TO home_category_news;
class Category_news(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='Название категории')
 
    class Meta:
        verbose_name = 'Категория новостей'
        verbose_name_plural = 'Категории новостей'
        ordering = ['name']

    def __str__(self):
        return self.name

class News(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    photo = models.ImageField(upload_to="home/img/%Y/%m/%d/", blank = True, verbose_name='Главное фото')
    short_description = models.TextField(max_length=255, blank=True, verbose_name='Краткое описаниеписание')
    content = models.TextField(blank=True, verbose_name='Тема стстьи')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')
    num_top = models.IntegerField(default=0, verbose_name='Номер в топе')
    is_published = models.BooleanField(default=True, verbose_name='Опубликована')
    author = models.ForeignKey(CustomUser, related_name='author_create_news', editable=False, on_delete=models.CASCADE, verbose_name='Автор')
    author_last_update = models.ForeignKey(CustomUser,blank = True, null=True, related_name='author_update_news', editable=False, on_delete=models.CASCADE, verbose_name='Автор изменения')
    cat = models.ForeignKey(Category_news, on_delete=models.PROTECT, verbose_name='Категория новостей')
    # e = models. ArrayField(models.CharField(max_length=200), blank=True)
    # title1 = models.CharField(blank = True, null=True, max_length=255, verbose_name='Заголовок1')
    # photo1 = models.ImageField(upload_to="home/img/%Y/%m/%d/", blank = True, verbose_name='Фото 1', null=True)
    # text1 = models.TextField(blank=True, verbose_name='Текст 1', null=True)
    # title2 = models.CharField(blank = True, null=True, max_length=255, verbose_name='Заголовок2')
    # photo2 = models.ImageField(upload_to="home/img/%Y/%m/%d/", blank = True, verbose_name='Фото 2', null=True)
    # text2 = models.TextField(blank=True, verbose_name='Текст 2', null=True)
    # title3 = models.CharField(blank = True, null=True, max_length=255, verbose_name='Заголовок3')
    # photo3 = models.ImageField(upload_to="home/img/%Y/%m/%d/", blank = True, verbose_name='Фото 3', null=True)
    # text3 = models.TextField(blank=True, verbose_name='Текст 3', null=True)
    # title4 = models.CharField(blank = True, null=True, max_length=255, verbose_name='Заголовок4')
    # photo4 = models.ImageField(upload_to="home/img/%Y/%m/%d/", blank = True, verbose_name='Фото 4', null=True)
    # text4 = models.TextField(blank=True, verbose_name='Текст 4', null=True)
    # title5 = models.CharField(blank = True, null=True, max_length=255, verbose_name='Заголовок5')
    # photo5 = models.ImageField(upload_to="home/img/%Y/%m/%d/", blank = True, verbose_name='Фото 5', null=True)
    # text5 = models.TextField(blank=True, verbose_name='Текст 5', null=True)
    # title6 = models.CharField(blank = True, null=True, max_length=255, verbose_name='Заголовок6')
    # photo6 = models.ImageField(upload_to="home/img/%Y/%m/%d/", blank = True, verbose_name='Фото 6', null=True)
    # text6 = models.TextField(blank=True, verbose_name='Текст 6', null=True)
    # contents_style  =  models.JSONField(null=True, blank = True, verbose_name='Стили контента')
    contents_style  =  models.TextField(null=True, blank=True, verbose_name='Стили контента')
    contents_script = models.TextField(null=True, blank=True, verbose_name='Скрипт контента')
    contents = models.TextField(null=True, blank=True, verbose_name='Дополнительный контент')
    
    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['time_create', 'title']

    def __str__(self):
        return self.title
    
    
    # def delete(self, using=None, keep_parents=False):
    #     self.image.delete()
    #     super().delete()
    
    def get_absolute_url(self):
        return reverse('home', kwargs={'post_id': self.pk})
    
    def get_absolute_url_media(self):
        # return reverse('home', kwargs={'post_id': self.pk})
        media_path = os.path.abspath("../company101/media/")
        # print(media_path)
        return media_path