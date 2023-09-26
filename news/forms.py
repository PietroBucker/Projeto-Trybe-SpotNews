from django import forms

# from news.models.category_model import Categories

# from news.models.news_model import News


class CreateCategoryModelForm(forms.Form):
    name = forms.CharField(max_length=200, required=True, label='nome')
