from django.urls import path, re_path

from .views import *

urlpatterns = [
    path('', index),
    path('news/<int:news_id>/', news),
    # path('create-news-article/', create_news_article, name='create_news_article'),
    # path('news/<int:pk>/', news_detail, name='news_detail'),
    
    # path('about/', about),
    # path('cats/<slug:cat>/', categories),
    # re_path(r'^archive/(?P<year>[0-9]{4})/', archive),

]
