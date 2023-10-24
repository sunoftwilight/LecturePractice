# if~else 조건문
a = 3

if a>3:
    print('3 초과')
else :                      # else는 필요한 경우에만 사용하면 됨!
    print('3 이하')

print(a)


# else 조건이 필요없는 if문
num = 2
if num < 0 :
    num = num * -1
print(num)


# 복수 + 중첩 조건문
dust = 35

if dust > 150:
    print('매우 나쁨')
    if dust > 300:
        print('위험해요! 나가지 마세요!')    # dust > 300 이면 '매우나쁨' + '위험해요' 모두 출력
elif dust > 80:
    print('나쁨')
elif dust > 30:
    print('보통')
else:
    print('좋음')


# for 반복문
items = ['apple', 'banana', 'coconut']

for item in items:
    print(item)


# 문자열 순회
country = 'Korea'           # list('Korea')로 변화하지 않아도 slicing됨

for char in country:
    print(char)


# 인덱스로 리스트 순회
numbers = [4, 6, 10, -8, 5]

for i in range(len(numbers)):
    numbers[i] = numbers[i] * 2

print(numbers)

# print(list(map(lambda i: i * 2, numbers)))
# 위의 for문 실행 결과와 동일한 결과 출력


# 중첩된 반복문
outers = ['A', 'B']
inners = ['c', 'd']

for outer in outers:
    for inner in inners:
        print(outer, inner)


# 중첩 리스트 순회
elements = [['A', 'B'], ['c', 'd']]

for elem in elements:
    print (elem)


# while문
A = 0               # 초기값

while A < 3:        # 조건식
    print(A)
    A += 1          # 증감식

print("끝")


# break를 통한 반복문 탈출
numbers = [1, 3, 5, 6, 7, 9, 10, 11]
is_even = False

for num in numbers:
    # 짝수를 만나면
    if num % 2 == 0 :
        print('첫 번째 짝수입니다. : ', num)
        is_even = True
        break
if not is_even:         # 짝수가 있을 경우 if not True 는 False이므로 출력 X
                        # 짝수가 없을 경우 if not False가 되어 True이므로 출력 O
    print('짝수를 찾지 못했습니다.')


# List Comprehension
# LC - for
numbers = [1, 2, 3, 4, 5]
squared_nums = [num ** 2 for num in numbers]

print(squared_nums)

# LC - if
results = [i for i in range(10) if i % 2 == 0]
print(results)