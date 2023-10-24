my_set = {1, 2, 3}
# my_set.discard(2)

# print(my_set)

# my_set.remove(10)
print(my_set.discard(10))

my_set = {1, 2, 3}
element = my_set.pop()
print(element)
print(my_set)

my_set2 = {'a', 'b', 'c'}
element2 = my_set2.pop()
print(element2)
print(my_set2)

person = {'name': 'Alice', 'age': 25}

print(person.get('name'))                  # Alice
print(person.get('country'))               # None
print(person.get('country', 'Unknown'))    # None


print(person.keys())
for key in person.keys():
    print(key)


print(person.values())        # dict_keys(['name', 'age']) - key가 리스트로 나옴
for v in person.values():   # value만 뽑아내고 싶다 -> for문 이용
    print(v)


# print(person.pop('age'))  
print(person) 
print(person.pop('country', None)) 
print(person.pop('country', '해당 키는 없어요')) 
# print(person.pop('country'))

# print(person.setdefault('country', 'KOREA'))   # KOREA
print(person)


person = {'name': 'Alice', 'age': 25}
other_person = {'name': 'Jane', 'gender': 'Female'}

person.update(other_person)
print(person)  

person.update(age=50)
print(person) 

person.update(country='KOREA')
print(person)


original_list = [1, 2, 3]
copy_list = original_list
print(original_list, copy_list) 

copy_list[0] = 'hi'
print(original_list, copy_list)


a = [1, 2, 3]
b = a[:]           # 방법 1 - 슬라이싱
print(a, b) 

b[0] = 100
print(a, b)        #[1, 2, 3] [100, 2, 3]

c = a.copy()       # 방법 2 - 내장함수 copy
c[0] = 100
print(a, c)        #[1, 2, 3] [100, 2, 3]


import copy    # 깊은 복사는 파이썬 모듈 copy의 deepcopy 메소드 필요


original_list = [1, 2, [1, 2]]
deep_copied_list = copy.deepcopy(original_list)

deep_copied_list[2][0] = 100

print(original_list) 
print(deep_copied_list)