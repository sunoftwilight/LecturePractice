from django.shortcuts import render, redirect
from .models import Article


# Create your views here.
def index(request):
    articles = Article.objects.all()

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
    title = request.POST.get('title')
    content = request.POST.get('content')

    # 1. 제목, 내용 하나씩 입력 받은 후 save
    # article = Article()
    # article.title = title
    # article.content = content
    # article.save()

    # 2. 제목, 내용 동시에 입력 받은 후 save
    article = Article(title=title, content=content)
    article.save()

    # 3. 제목, 내용 입력 및 저장 한번에
    # Article.object.create(title=title, content=content)

    # return render(request, 'articles/create.html')
    return redirect('articles:index')


def delete(request, pk):
    # 바로 삭제 불가 - 몇 번 게시글 삭제할 건지 조회 먼저 !!!
    article = Article.objects.get(pk=pk)

    # 조회한 게시글을 삭제
    article.delete()
    return redirect('articles:index')


def edit(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/edit.html', context)


def update(request, pk):
    title = request.POST.get('title')
    content = request.POST.get('content')

    # 수정하고자 하는 게시글을 조회
    article = Article.objects.get(pk=pk)
    article.title = title
    article.content = content
    article.save()

    return redirect('articles:detail', article.pk)