from django.http import HttpResponseNotFound, JsonResponse
import json
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from home.models import News
from market.models import Product
from service.models import Service
from django.db.models import Q
from django.forms.models import model_to_dict


def index(request):
    return render(request, '/search/search.html')


@csrf_exempt
def get_search_str(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode("utf-8"))
        str = data['str']
        select = data['select']
        news = []
        product = []
        service = []
        if select == "all" or select == "news":
            news = News.objects.filter(Q(title__icontains=str) | Q(short_description__icontains=str) | Q(cat__name__icontains=str)).values('id', 'title', 'short_description')
        if select == "all" or select == "product":    
            product = Product.objects.filter(Q(model__icontains=str) | Q(manufacturer__icontains=str) | Q(short_description__icontains=str) | Q(cat__name__icontains=str)).values('id', 'model', 'manufacturer', 'short_description', 'cat')
        if select == "all" or select == "service":    
            service = Service.objects.filter(Q(name__icontains=str) | Q(short_description__icontains=str) | Q(cat__name__icontains=str)).values('id', 'name', 'short_description', 'cat')
        
        return JsonResponse({'news': list(news), 'product': list(product), 'service': list(service)})
    else:
        return HttpResponseNotFound('404')
 