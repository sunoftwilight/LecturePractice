numbers = [1, 2, 3]

# 1. 할당
list1 = numbers

# 2. 슬라이싱
list2 = numbers[:]


numbers[0] = 100

print(list1)       # [100, 2, 3]
print(list2)       # [1, 2, 3]