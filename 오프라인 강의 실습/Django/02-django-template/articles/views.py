from django.shortcuts import render
import random


# Create your views here.
def index(request):
    return render(request, 'articles/index.html')


def dinner(request):
    foods = ['돼지갈비찜', '차돌된장찌개']
    picked = random.choice(foods)
    context = {
        'foods': foods,
        'picked': picked,
    }
    return render(request, 'articles/dinner.html', context)


def search(request):
    return render(request, 'articles/search.html')


def throw(request):
    return render(request, 'articles/throw.html')


def catch(request, ):
    context = {
        'message': request.GET.get('message')
    }
    return render(request, 'articles/catch.html', context)


def hello(request, name):
    context = {
        'name': name,
    }
    return render(request, 'articles/hello.html', context)