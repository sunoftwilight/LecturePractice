'''
9
3 2 4 6 9 1 8 7 5
'''


def hoare_partition(a, l, r):
    p = a[l]
    i, j = l, r
    while i <= j:
        # 왼쪽에서 큰 값
        while i <= j and a[i] <= p: i += 1
        # 오른쪽에서 작은 값
        while i <= j and a[i] >= p: i -= 1
        # i <-> j swap
        if i < j: a[i], a[j] = a[j], a[i]

    # pivot과 j의 값을 교환
    a[l], a[j] = a[j], a[l]

    return j    # pivot의 자리


def quick_sort(a, l, r):
    if l < r:
        pivot = hoare_partition(a, l, r)
        # pivot 제외하고 sort
        quick_sort(a, l, pivot - 1)
        quick_sort(a, pivot + 1, r)


N = int(input())
arr = list(map(int, input().split()))
quick_sort(arr, 0, len(arr)-1)
print(arr)                 # [1, 2, 3, 4, 5, 6, 7, 8, 9]
