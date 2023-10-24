# find & index
print('banana'.find('a'))      # 1
print('banana'.find('an'))     # 1
print('banana'.find('z'))      # -1
print('banana'.index('a'))     # 1
print('banana'.index('an'))    # 1
# print('banana'.index('z'))   # ValueError: substring not found
print('=========================')


# isupper & islower
string1 = 'HELLO'
string2 = 'Hello'

print(string1.isupper())     # True
print(string2.isupper())     # False
print(string1.islower())     # False
print(string2.islower())     # Flase
print('=========================')


# isalpha
string3 = 'Hello'
string4 = '123'
string5 = '안녕'
print(string3.isalpha())     # True
print(string4.isalpha())     # False
print(string5.isalpha())     # True
print('=========================')


# replace
text = 'Hello, world!'
new_text = text.replace('world', 'Python')     # 원본은 변경되지 않으므로 새로운 값에 할당해서 반환받아야함!
print(new_text, text)        # Hello, Python! Hello, world!
print('=========================')


# strip
text2 = '         Hello, world         '
new_text2 = text2.strip()
print(new_text2, text2)     # Hello, world          Hello, world
print('=========================')


# split
text3 = 'Hello, world!'
words = text3.split(',')
print(words, type(words))    # ['Hello', ' world!'] <class 'list'>
print('=========================')


# join
words = ['Hello', 'world!']
texts = '-'.join(words)
print(texts)                 # Hello-world!

text_other = 'Komputer'
print(text_other, type(text_other))      # Komputer <class 'str'>
lst = list(text_other)
print(lst, type(lst))                    # ['K', 'o', 'm', 'p', 'u', 't', 'e', 'r'] <class 'list'>
lst[0] = 'C'
print(lst, type(lst))                    # ['C', 'o', 'm', 'p', 'u', 't', 'e', 'r'] <class 'list'>
text_other = ''.join(lst)         
print(text_other, type(text_other))      # Computer <class 'str'>
print('=========================')


lst2 = [1, 2, 3, 4]
print(''.join(map(str, lst2)), type(''.join(map(str, lst2))))
print('=========================')


# capitalize & title & upper & swapcase
text0 = 'heLLo, woRld!'
new_text1a = text0.capitalize()
new_text2b = text0.title()
new_text3c = text0.upper()
new_text4d = text0.swapcase()

print(new_text1a) # Hello, world!
print(new_text2b) # Hello, World!
print(new_text3c) # HELLO, WORLD!
print(new_text4d) # HEllO, WOrLD!

text_1 = 'heLLo, woRld!'
new_text_1 = text_1.swapcase().replace('l', 'z')
print(new_text_1) # HEzzO, WOrLD!
print('=========================')


# append & extend & insert & remove & pop & clear
my_list = [1, 2, 3]

my_list.append(4)
print(my_list)                   # [1, 2, 3, 4]

my_list.extend([5, 6, 7]) 
print(my_list)                   # [1, 2, 3, 4, 5, 6, 7]

my_list.insert(1, 5)           
print(my_list)                   # [1, 5, 2, 3, 4, 5, 6, 7]

my_list.remove(5)
print(my_list)                   # [1, 2, 3, 4, 5, 6, 7]

print(my_list.pop(-1))           # 7
print(my_list.pop(0))            # 1
print(my_list)                   # [2, 3, 4, 5, 6]

my_list.clear()
print(my_list)                   # []
print('=========================')


# index 
my_list = [1, 2, 3]
# idx = my_list.index(4)       # ValueError: 4 is not in list
# print(idx)
idx = my_list.index(2)         # 1
print(idx)
print('=========================')


# count 
my_list = [1, 2, 2, 2, 3, 3]
idx = my_list.count(2)         # 3
print(idx)

def my_count(item):            # for과 if를 이용한 count 함수
    count = 0
    for num in my_list:
        if num == item:
            count += 1
    return count
print(my_count(3))             # 2
print('=========================')


# sort 
my_list = [3, 2, 1, 2, 1, 4]
my_list.sort()
print(my_list)                   # [1, 1, 2, 2, 3, 4]   .sort 메서드 : 파괴 메서드
my_list.sort(reverse=True)
print(my_list)                   # [4, 3, 2, 2, 1, 1]

my_list2 = [3, 2, 1]
print(sorted(my_list2))          # [1, 2, 3]  
print(my_list2)                  # [3, 2, 1]     sorted 함수 : 비파괴 함수 - 원본 보존

my_list3 = [
    ['홍', '35', 'seoul'],
    ['김', '25', 'gumi'],
    ['이', '30', 'daegu']
]
my_list3.sort()
print(my_list3)    # [['김', '25', 'gumi'], ['이', '30', 'daegu'], ['홍', '35', 'seoul']]      : 2차원 배열은 기본적으로 가장 앞 요소를 기준으로 sorting 됨!

my_list3.sort(key = lambda x: x[2])      # sort의 기본형태 sort(key=None, reverse=False)
print(my_list3)    # [['이', '30', 'daegu'], ['김', '25', 'gumi'], ['홍', '35', 'seoul']]      : key를 통해 index 지정해주면 다른 요소를 기준으로 sorting 가능!
print('=========================')


# reverse
my_list = [1, 3, 2, 8, 1, 9]
my_list.reverse()
print(my_list)         # [9, 1, 8, 2, 3, 1]
