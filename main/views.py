from django.http import HttpResponse
from django.shortcuts import render

from goods.models import Categories


def index(request):

    categories = Categories.objects.all()

    context = {
        "title": "Home",
        "content": "Магазин мебели OKEA",
        "categories": categories,
    }
    return render(request, "main/index.html", context)


def about(request):
    context = {
        "title": "О нас",
        "content": "О нас",
        "text_on_page": "Текст о том почему этот магазин крутой",
    }
    return render(request, "main/about.html", context)