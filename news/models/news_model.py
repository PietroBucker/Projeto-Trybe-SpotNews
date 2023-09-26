from django.db import models
from news.models.category_model import Categories

from news.models.user_model import Users
from news.validators import validate_min_words


class News(models.Model):
    title = models.CharField(max_length=200, validators=[validate_min_words])
    content = models.TextField()
    created_at = models.DateField()
    image = models.ImageField(
        upload_to="img/", null=True, blank=True
    )
    author = models.ForeignKey(
        Users, on_delete=models.CASCADE, related_name="news"
    )
    categories = models.ManyToManyField(
        Categories, related_name="news"
    )

    def __str__(self) -> str:
        return self.title
