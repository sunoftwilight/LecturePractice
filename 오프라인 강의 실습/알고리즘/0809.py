# 재귀함수 - factorial

def factorial(n):
    # 기본파트 : 멈추는 부분
    if n == 1:
        return 1

    # 유도파트 : 재귀 호출
    else:
        return n * factorial(n-1)


print(factorial(4))
