from django.shortcuts import render

from news.models.news_model import News

# Create your views here.


def index(request):
    news = {'news': News.objects.all()}
    return render(request, "home.html", news)
