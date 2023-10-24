from django.shortcuts import render
import random


# Create your views here.
def index(request):
    context = {
        'name' : 'Jane',
    }
    return render(request, 'articles/index.html', context)


def dinner(request):     # request 대신 다른 변수를 써도 기능상 문제 없으나, request로 고정적인 사용을 하는 것이 개발자끼리의 약속임
    foods = ['국밥', '국수', '카레', '탕수육',]
    picked = random.choice(foods)
    empty_list = []
    context = {
        'foods' : foods,
        'picked' : picked,
        'empty_list' : empty_list
    }
    return render(request, 'articles/dinner.html', context)


def search(request):
    return render(request, 'articles/search.html')


def throw(request):
    return render(request, 'articles/throw.html')


def catch(request):
    message = request.GET.get('message')
    context = {
        'message' : message,
    }
    # 사용자로부터 요청을 받고,
    # 요청에서 사용자의 입력 데이터를 찾은 후,
    # context에 저장 한 뒤, catch 템플릿에 출력
    return render(request, 'articles/catch.html', context)


def greeting(request, name):
    context = {
        'name' : name,

    }
    return render(request, 'articles/greeting.html', context)


def detail(request, num):
    context = {
        'num' : num,
    }
    return render(request, 'articles/detail.html', context)