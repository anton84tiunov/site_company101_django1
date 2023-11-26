from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.utils import timezone
from .models import News
# from .forms import NewsArticleForm

def index(request):
    news = News.objects.all()
    print(news)
    return render(request, 'home/home.html', {'news': news})

def news(request, news_id):
    news = News.objects.get(pk=news_id)
    # if news.contents_style:
    #     sort_news =  dict(sorted(news.contents_style.items()))
    #     news.contents_style = sort_news

    return render(request, 'home/news.html', {'news': news})


# @login_required
# def create_news_article(request):
#     if request.method == 'POST':
#         form = NewsArticleForm(request.POST, request.FILES)
#         if form.is_valid():
#             news_article = form.save(commit=False)
#             news_article.author = request.user
#             news_article.save()
#             return redirect('news_detail', pk=news_article.pk)
#     else:
#         form = NewsArticleForm()
#     return render(request, 'create_news_article.html', {'form': form})

# def news_detail(request, pk):
#     news_article = News.objects.get(pk=pk)
#     return render(request, 'news_detail.html', {'news_article': news_article})
