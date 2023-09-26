from django.urls import path
from news.views import details, index


urlpatterns = [
    path("", index, name="home-page"),
    path("news/<int:news_id>", details, name='news-details-page')
    ]
