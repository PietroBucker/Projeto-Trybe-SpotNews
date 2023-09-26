from django.contrib import admin
from news.models.category_model import Categories

from news.models.news_model import News
from news.models.user_model import Users

# Register your models here.
admin.site.site_header = "SpotNews"
admin.site.register(News)
admin.site.register(Users)
admin.site.register(Categories)
