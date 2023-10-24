# 진법 변경

print(bin(12))


# 지수(제곱횟수) 표현 10^
print(314e-2)
print(314e2)


# f-string
print('Debugging roaches 13 living room')

bugs = 'roaches'
counts = 13
area = 'living room'
print(f'Debugging {bugs} {counts} {area}')

#formatting의 옛날 방식
print('Debugging {} {} {}'.format(bugs, counts,area))
print('Debugging %s %d %s' % (bugs, counts,area))

# f-string 응용 
greeting = 'hi'
print(f'{greeting:^10}')  # greeting을 10 글자 중 가운데에 위치하도록 하는 코드
print(f'{greeting:>10}')  # greeting을 10 글자 중 오른쪽에 위치하도록 하는 코드
print(f'{3.141592:.4f}')  # 소수점 4째자리까지만 표현하는 코드


# 불변과 가변
my_str = 'hello'
#my_str[0] = 'z'

my_list = [1, 2, 3]
my_list[0] = 100       # 0번째 요소를 100으로 변경
print(my_list)


# 형 변환 (가변)
list_1 = [1, 2, 3]
list_2 = list_1

list_1[0] = 100
print(list_1)   # [100, 2, 3]
print(list_2)   # [100, 2, 3]

# 형 변환 (불변)
x = 10
y = x

x= 20
print(x)
print(y)