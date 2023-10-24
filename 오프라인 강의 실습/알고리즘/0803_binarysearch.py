def binary_search(a, n, key):
    start = 0
    end = n - 1
    while start <= end:
        mid = (start + end) // 2
        # 1. middle = key
        if a[mid] == key:
            return True, mid
        # 2. middle > key
        elif a[mid] > key:
            end = mid - 1
        # 3. middle < key
        else:
            start = end + 1
    return False, -1   # 보통 -1을 주는데 파이썬은 -1 인덱스가 존재하므로 False로 주는 것이 안전


key = 7
arr = [2, 4, 7, 9, 11, 19, 23]
print(binary_search(arr, len(arr), key))
