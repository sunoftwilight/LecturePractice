# atoi_itoa  (array to integer / integer to array)

def itoa(num):                 # 123
    arr = []
    value = 0
    while num:
        value = num % 10       # 3     2   1
        num //= 10             # 12    1   0
        arr.append(value)      # | 3 | 2 | 1 |
    
    arr.reverse()   
    
    return arr


def atoi(num):      # | 3 | 2 | 1 |
    value = 0
    for i in range(len(arr)):
        value = value * 10 + arr[i]     # 0 * 10 + 3 = 3 
                                        # 3 * 10 + 2 = 32 
                                        # 32 * 10 + 1 = 321
    return value


num = 123
arr = itoa(num)
print(arr)
# arr[0], arr[-1] = arr[-1], arr[0]
# print(arr)
arr = atoi(num)
print(arr)