from django.shortcuts import redirect, render, get_object_or_404
from django.http import Http404
from news.forms import CreateCategoryModelForm, CreateNewsModelForm
from news.models.category_model import Categories
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


def create_category(request):
    form = CreateCategoryModelForm()
    if request.method == "POST":
        form = CreateCategoryModelForm(request.POST)
        if form.is_valid():
            Categories.objects.create(**form.cleaned_data)
            return redirect("home-page")

    context = {"form": form}

    return render(request, "categories_form.html", context)


def create_news(request):
    form = CreateNewsModelForm()
    if request.method == "POST":
        form = CreateNewsModelForm(request.POST, request.FILES)

        if form.is_valid():
            # news_instance = form.save(commit=False)
            # news_instance.save()
            # news_instance.categories.set(form.cleaned_data["categories"])

            form.save()
            return redirect("home-page")

    context = {"form": form}

    return render(request, "news_form.html", context)
