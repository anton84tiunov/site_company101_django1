from django.db import models

from home.models import CustomUser

class Category_product(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='Название категории')
 
    class Meta:
        verbose_name = 'Категория товара'
        verbose_name_plural = 'Категории товаров'
        ordering = ['name']

    def __str__(self):
        return self.name

class Product(models.Model):
    manufacturer = models.CharField(max_length=255, verbose_name='Производитель')
    model = models.CharField(max_length=255, verbose_name='модель')
    photo = models.ImageField(upload_to="market/img/%Y/%m/%d/", blank = True, verbose_name='Главное фото')
    short_description = models.TextField(max_length=255, blank=True, verbose_name='Краткое описаниеписание')
    price = models.IntegerField(default=0, verbose_name='Цена')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')
    num_top = models.IntegerField(default=0, verbose_name='Номер в топе')
    is_availability = models.BooleanField(default=True, verbose_name='В наличии')
    is_published = models.BooleanField(default=True, verbose_name='Опубликована')
    author = models.ForeignKey(CustomUser, related_name='author_create_product', editable=False, on_delete=models.CASCADE, verbose_name='Автор')
    author_last_update = models.ForeignKey(CustomUser,blank = True, null=True, related_name='author_update_product', editable=False, on_delete=models.CASCADE, verbose_name='Автор изменения')
    cat = models.ForeignKey(Category_product, on_delete=models.PROTECT, verbose_name='Категория товара')
    extended_description  =  models.TextField(null=True, blank=True, verbose_name='подробное описание')
    characteristics  =  models.TextField(null=True, blank=True, verbose_name='характеристики')


    
    class Meta:
            verbose_name = 'Товар'
            verbose_name_plural = 'Товары'
            ordering = ['time_create', 'model', 'price']

    def __str__(self):
        return self.model
