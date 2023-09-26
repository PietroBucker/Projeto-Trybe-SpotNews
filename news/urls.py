from django.urls import path
from news.views import create_category, create_news, details, index


urlpatterns = [
    path("", index, name="home-page"),
    path("news/<int:news_id>", details, name='news-details-page'),
    path("categories", create_category, name='categories-form'),
    path("news", create_news, name='news-form'),
    ]
