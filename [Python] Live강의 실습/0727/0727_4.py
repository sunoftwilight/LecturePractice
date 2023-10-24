try :
    num = int(input('100으로 나눌 값을 입력해: '))
    print(100 / num)
except BaseException :
    print('숫자를 입력하라고')
except ZeroDivisionError :
    print('왜 0을 입력하는거야??')
except :
    print('에러가 발생했어')


# BaseException은 ZeroDivisionError의 상위 클래스로 설계되어 있음
# 따라서 0을 입력해도 무조건 BaseException에서 실행되고,
# 하위 클래스인 ZeroDivisionError 블록으로 넘어가지 못함