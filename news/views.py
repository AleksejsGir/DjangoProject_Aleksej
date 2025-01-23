from django.http import HttpResponse
from django.shortcuts import render

info = {
    "users_count": 100600,
    "news_count": 100600,
    "menu": [
        {"title": "Главная", "url": "/", "url_name": "index"},
        {"title": "О проекте", "url": "/about/", "url_name": "about"},
        {"title": "Каталог", "url": "/catalog/", "url_name": "catalog"},
    ]
}

def main(request):
    return HttpResponse('Hello, world!')  # Вернёт страницу с надписью "Hello world!"


def info(request):
    return HttpResponse('information page')


def get_all_news(request):
    return render(request, 'news/catalog.html')


def get_news_by_id(request, news_id):
    if news_id > 10:
        return HttpResponse('Такой новости нет', status=404)
    return HttpResponse(f'Вы открыли новость {news_id}')  # Вернёт страницу с надписью "Вы открыли новость {news_id}"