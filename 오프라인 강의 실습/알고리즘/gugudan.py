# 구구단 작성

# for문
for i in range(2,10):
    print(f'== {i}단 =======')
    for k in range(1,10):
       print(f'  {i} x {k} = {i*k}')
       if i == 9 and k == 9:
             print('==============')


# while문
a = 2
while a < 10 :
    print(f'== {a}단 =======')
    b = 1                              

    while  b < 10 :
        print(f'  {a} x {b} = {a*b}')
        b += 1  

    if a == 9 and b == 10 :
        print('==============')    

    a += 1

# b = 1을 a = 2 다음줄에 적으면 2단에서 b = 9가 된 후 초기화가 되지않고 b+=1에 의해 10이 됨. 
# => while 종료되므로 2단까지만 출력함. 따라서 초기화 초기값 선언을 무조건 최상단에 하는 것은 금물!!