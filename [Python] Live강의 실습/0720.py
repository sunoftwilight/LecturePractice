"""
num = int(input('숫자를 입력하세요: '))

# if statement
# num이 홀수라면
if num % 2 == 1 :            # if num % 2 : 를 해도 결과 같음 (결과 == 1 == True이므로) 
                             #  단, == 1 을 써주는 것이 훨씬 명시적인 코드임.
    print('홀수입니다.')
# num이 홀수가 아니라면 (=짝수면)
else :
    print('짝수입니다.')

country = set('Korea')

for char in country:
    print(char)
"""
"""
# 0~9 요소를 가지는 리스트 만들기
# 1. 일반적인 방법
new_lsit = []
for i in range(10):
    if i % 2 == 1:
        new_lsit.append(i)
print(new_lsit)

# 2. List Comprehension
new_lsit_2 = [i for i in range(10) if i % 2 == 1]
new_lsit_3 = [i if i % 2 == 1 else str(i) for i in range(10)]
print(new_lsit_2)
print(new_lsit_3)
"""


# 리스트 생성하는 3가지 방법 비교 - 어떤것이 most fast?
# 정수 1,2,3을 가지는 새로운 리스트 만들기

numbers = ['1', '2',  '3']

# 1. for loop
new_numbers = []
for number in numbers:
    new_numbers.append(int(number))

print(new_numbers)     # [1, 2, 3]


# 2. map
new_numbers_2 = list(map(int, numbers))
print(new_numbers_2)     # [1, 2, 3]


# 3. List Comprehension
new_numbers_3 = [int(number) for number in numbers]
print(new_numbers_3)     # [1, 2, 3]


#enumerate
result = ['a', 'b', 'c']

print(enumerate(result))        # <enumerate object at 0x000002BC7CB73700>
print(list(enumerate(result)))  # [(0, 'a'), (1, 'b'), (2, 'c')]

for index, elem in enumerate(result):
    print(index, elem)
