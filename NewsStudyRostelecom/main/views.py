from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from django.db import connection, reset_queries
from news.models import Article
def index(request):
    from django.db.models import Count, Avg, Max
    from django.contrib.auth.models import User
    max_article_count_user = User.objects.annotate(Count('article', distinct=True)).order_by('-article__count').first()
    print(max_article_count_user)
    max_article_count =  User.objects.annotate(Count('article', distinct=True)).aggregate(Max('article__count'))
    max_article_count_user2 = User.objects.annotate(Count('article', distinct=True)).filter(article__count__exact=max_article_count['article__count__max'])
    print(max_article_count_user2)
    return render(request,'main/index.html')
    #return render(request, 'main/news.html')

# def index(request):
#
#     from django.db.models import Count, Avg, Max
#     from django.contrib.auth.models import User
#
#     max_article_count_user = User.objects.annotate(Count('article', distinct=True)).order_by('-article__count').first()
#     print(max_article_count_user)
#     max_article_count =  User.objects.annotate(Count('article', distinct=True)).aggregate(Max('article__count'))
#     max_article_count_user2 = User.objects.annotate(Count('article', distinct=True)).filter(article__count__exact=max_article_count['article__count__max'])
#     print(max_article_count_user2)
#     return render(request,'main/index.html')

def news(request):
    return render(request,'main/news.html')

def news_1(request):
    return render(request,'main/news_1.html')


def examples(request):
    if request.method == 'POST':
        print('Получили post-Запрос!')
        print(request.POST)
        title = request.POST.get('title')
        price = request.POST.get('price')
        quantity = request.POST.get('quantity')
        new_product = Product(title,float(price),int(quantity))
        print('Создан товар:',new_product.title, 'Общая сумма:',new_product.amount())
    else:
        print('Получили get-Запрос!')
    water = Product('Добрый-минералка', 43, 2)
    chocolate = Product('Шоколадка', 80, 1)

    colors = ['red','blue','golden','black']
    context = {
        'colors':colors,
        'water': water,
        'chocolate':chocolate,
    }
    return render(request,'main/examples.html', context)

def get_demo(request,a,operation,b):
    match operation:
        case 'plus':
            result = int(a)+ int(b)
        case 'minus':
            result = int(a) - int(b)
        case 'multiply':
             result = int(a) * int(b)
        case 'divide':
            result = int(a) / int(b)
        case _:
            return HttpResponse(f'Неверная команда')
    return HttpResponse(f'Вы ввели: {a} и {b} <br>Результат {operation}: {result}')


def about(request):
    return HttpResponse('<h1> о нас </h1>')


def contacts(request):
    return HttpResponse('<h1> контакты </h1>')


def sidebar(request):
    return render(request,'main/sidebar.html')


def custom_404(request, exception):
    # return render(request,'main/sidebar.html')
    return HttpResponse(f'405-1=404:{exception}')