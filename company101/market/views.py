from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Product



def index(request):
    product = Product.objects.all()
    # print(product)
    return render(request, 'market/market.html', {'product': product})

def product(request, product_id):
    product = Product.objects.get(pk=product_id)
    # if news.contents_style:
    #     sort_news =  dict(sorted(news.contents_style.items()))
    #     news.contents_style = sort_news

    return render(request, 'market/product.html', {'product': product})