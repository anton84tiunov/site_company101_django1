from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Service



def index(request):
    service = Service.objects.all()
    return render(request, 'service/services.html', {'service': service})

def service(request, service_id):
    service = Service.objects.get(pk=service_id)
    # if news.contents_style:
    #     sort_news =  dict(sorted(news.contents_style.items()))
    #     news.contents_style = sort_news

    return render(request, 'service/service.html', {'service': service})
