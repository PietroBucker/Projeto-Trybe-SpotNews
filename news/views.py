from django.shortcuts import render, get_object_or_404
from django.http import Http404
from news.models.news_model import News

# Create your views here.


def index(request):
    news = {"news": News.objects.all()}
    return render(request, "home.html", news)


def details(request, news_id):
    try:
        new = get_object_or_404(News, id=news_id)
        return render(request, "news_details.html", {"new": new})
    except Http404:
        return render(request, "404.html")
