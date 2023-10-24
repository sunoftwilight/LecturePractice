from django.shortcuts import render, redirect
from .models import Article


# Create your views here.
def index(request):
    # 예전에 적은 글이 제일 위로 오게 표시
    # articles = Article.objects.all()

    # 최근에 적은 글이 제일 위로 오게 표시  (pk에 -를 붙여 불러오기)
    articles = Article.objects.order_by('-pk')
    context = {
        'articles': articles,
    }    
    return render(request, 'articles/index.html', context)


def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)


def new(request):
    return render(request, 'articles/new.html')


def create(request):
    # new에서 입력 넘겨받는 인자인 name을 각각 title, content로 설정함
    title = request.POST.get('title')
    content = request.POST.get('content')

    article = Article(title=title, content=content)
    article.save()

    # redirect는 variable routing처럼 url 접근함!!!
    return redirect('articles:detail', article.pk)


def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('articles:index')


def edit(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article': article,
    }

    return render(request, 'articles/edit.html', context)


def update(request, pk):
    article = Article.objects.get(pk=pk)
    article.title = request.POST.get('title')
    article.content = request.POST.get('content')
    article.save()

    return redirect('articles:detail', article.pk)