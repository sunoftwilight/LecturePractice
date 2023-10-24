my_set = {1, 2, 3, 40, 500, 6, 7, 'abc', 'Kim'}
my_set.add(4)
print(my_set)

# my_set.remove(30)   # KeyError: 30
my_set.discard(30)    # {1, 2, 3}

for _ in range(len(my_set)) :
    print(my_set.pop())