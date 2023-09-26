from datetime import date
from django import forms

from news.models.category_model import Categories

from news.models.news_model import News


class CreateCategoryModelForm(forms.Form):
    name = forms.CharField(max_length=200, required=True, label="Nome")


class CreateNewsModelForm(forms.ModelForm):
    class Meta:
        model = News
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["title"].label = "Título"
        self.fields["content"].label = "Conteúdo"
        self.fields["created_at"].label = "Criado em"
        self.fields["created_at"].widget = forms.DateInput(
            attrs={"type": "date"}
        )
        self.fields["created_at"].initial = date.today().strftime("%d/%m/%Y")
        self.fields["author"].label = "Autoria"
        self.fields["image"].label = "URL da Imagem"
        self.fields["categories"].label = "Categories"
        self.fields["categories"].widget = forms.CheckboxSelectMultiple(
            choices=[
                (category.id, category.name)
                for category in Categories.objects.all()
            ]
        )
