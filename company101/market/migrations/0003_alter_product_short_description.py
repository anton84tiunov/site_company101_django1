# Generated by Django 4.2.6 on 2023-11-25 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0002_alter_product_options_product_price_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='short_description',
            field=models.TextField(blank=True, max_length=255, verbose_name='Краткое описаниеписание'),
        ),
    ]
