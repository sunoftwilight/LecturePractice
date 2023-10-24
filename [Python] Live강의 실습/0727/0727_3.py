try :
    num = int(input('100으로 나눌 값을 입력해: '))
    print(100 / num)
except ValueError :
    print('숫자를 입력하라고')
except ZeroDivisionError :
    print('왜 0을 입력하는거야??')
# except (ValueError, ZeroDivisionError) :   # 한번에 작성하는 법
#     print('제대로 입력해라')
except :
    print('에러가 발생했어')