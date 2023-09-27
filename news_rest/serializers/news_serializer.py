from rest_framework import serializers

from news.models.news_model import News


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = [
            "id",
            "title",
            "content",
            "created_at",
            "image",
            "author",
            "categories",
        ]
